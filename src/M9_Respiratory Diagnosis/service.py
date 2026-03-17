import uuid
from datetime import datetime, date

from database import (
    insert_patient, insert_encounter, insert_symptom, 
    insert_cough_characteristic, insert_breath_sound
)
def process_encounter_data(patient, encounter, symptom, cough, breath, smoking, exposure):
    try:
        # Link relations using IDs
        patient_id = patient.get("PatientID", str(uuid.uuid4()))
        patient["PatientID"] = patient_id
        
        encounter_id = encounter.get("EncounterID", str(uuid.uuid4()))
        encounter["EncounterID"] = encounter_id
        encounter["PatientID"] = patient_id
        
        if "EncounterDate" not in encounter:
            encounter["EncounterDate"] = datetime.now()
        elif isinstance(encounter["EncounterDate"], date) and not isinstance(encounter["EncounterDate"], datetime):
            encounter["EncounterDate"] = datetime.combine(encounter["EncounterDate"], datetime.min.time())
            
        symptom["EncounterID"] = encounter_id
        cough["EncounterID"] = encounter_id
        breath["EncounterID"] = encounter_id
        
        smoking["PatientID"] = patient_id
        exposure["PatientID"] = patient_id

        insert_patient(patient)
        insert_encounter(encounter)
        insert_symptom(symptom)
        insert_cough_characteristic(cough)
        insert_breath_sound(breath)
        
        return {"success": True, "message": "Data linked successfully"}

    except Exception as e:
        return {"success": False, "message": str(e)}