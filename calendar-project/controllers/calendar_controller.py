import json
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
            required: true
            description: Transformation method to use.
          - name: user_mapping
            in: formData
            type: string
            required: false
            description: Optional JSON string with user-defined emoji mappings.
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
        method = request.form.get("method")


        user_mapping_json = request.form.get("user_mapping")

        user_mapping = None
        if user_mapping_json:
            try:
                user_mapping = json.loads(user_mapping_json)
                if not isinstance(user_mapping, dict):
                    raise ValueError("user_mapping must be a JSON object (dictionary).")
            except json.JSONDecodeError:
                return jsonify({"error": "Invalid JSON in user_mapping field."}), 400

        tmp_path = "tmp.ics"
        file.save(tmp_path)

        output_path = service.transform_calendar(tmp_path, method, user_mapping)

        return jsonify({"message": "Transformation complete", "file": output_path})

    except Exception as e:
        return jsonify({"error": str(e)}), 400