import base64
from io import BytesIO
from flask import Blueprint, request, jsonify, send_file
from services.calendar_service import CalendarService


calendar_bp = Blueprint("calendar", __name__)
service = CalendarService()

@calendar_bp.route("/transform", methods=["POST"])
def transform_calendar():
    """
        Transform an iCal (.ics) calendar to use emojis for events.
        ---
        tags:
          - Calendar
        consumes:
          - application/json
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              properties:
                file_base64:
                  type: string
                  description: Base64-encoded .ics file
                method:
                  type: string
                  enum: ["dictionary", "embedding"]
                  description: Transformation method
                user_mapping:
                  type: object
                  description: Optional user-defined emoji mappings
        responses:
          200:
            description: Transformed .ics file
            content:
              text/calendar:
                schema:
                  type: string
          400:
            description: Bad request
          500:
            description: Internal server error
        """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "JSON payload required"}), 400

        file_base64 = data.get("file_base64")
        method = data.get("method")
        user_mapping = data.get("user_mapping", None)

        if not file_base64 or not method:
            return jsonify({"error": "file_base64 and method are required"}), 400

        if method not in ["dictionary", "embedding"]:
            return jsonify({"error": f"Invalid method: {method}"}), 400

        # Decode base64 to BytesIO stream
        file_bytes = base64.b64decode(file_base64)
        input_stream = BytesIO(file_bytes)

        # Transform
        output_stream = service.transform_calendar_stream(input_stream, method, user_mapping)

        output_stream.seek(0)
        output_base64 = base64.b64encode(output_stream.read()).decode("utf-8")

        return jsonify({
            "message": "Transformation complete",
            "file_base64": output_base64
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500