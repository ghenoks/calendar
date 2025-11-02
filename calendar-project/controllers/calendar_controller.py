from flask import Blueprint, request, jsonify
from services.calendar_service import CalendarService


calendar_bp = Blueprint("calendar", __name__)
service = CalendarService()

@calendar_bp.route("/transform", methods=["POST"])
def transform_calendar():
    """
        Upload and transform a calendar file.
        ---
        consumes:
          - multipart/form-data
        parameters:
          - name: file
            in: formData
            type: file
            required: true
            description: The iCal (.ics) file to transform.
          - name: method
            in: formData
            type: string
            enum: ["dictionary", "regex", "embedding"]
            required: false
            description: Transformation method to use.
        responses:
          200:
            description: Transformation completed successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                file:
                  type: string
        """
    try:
        file = request.files["file"]
        method = request.form.get("method", "dictionary")

        tmp_path = "tmp.ics"
        file.save(tmp_path)

        output_path = service.transform_calendar(tmp_path, method)

        return jsonify({"message": "Transformation complete", "file": output_path})

    except Exception as e:
        return jsonify({"error": str(e)}), 400