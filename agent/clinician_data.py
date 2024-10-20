from enum import Enum
import json
from typing import List, Dict, Optional
import os

class CaseInsensitiveEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value.lower() == value.lower():
                return member
        return None

class Offices(CaseInsensitiveEnum):
    TYRONE = "Tyrone"
    DTSP = "DTSP"
    SARASOTA = "Sarasota"
    TAMPA = "Tampa"
    VIRTUAL = "Virtual - Everyone does virtual"

class Groups(CaseInsensitiveEnum):
    MINORS = "Minors"
    FAMILIES = "Families"
    COUPLES = "Couples"

class Modalities(CaseInsensitiveEnum):
    CBT = "CBT"
    EMDR = "EMDR"
    DBT = "DBT"
    EFT = "EFT"
    ACT = "ACT"
    ART = "ART"
    GOTTMAN_COUPLES_THERAPY = "Gottman Couples Therapy"
    ART_THERAPY = "Art Therapy"
    MINDFULNESS_BASED_THERAPY = "Mindfulness-Based Therapy"
    WALK_AND_TALK_THERAPY = "Walk and Talk Therapy"

class Specialties(CaseInsensitiveEnum):
    ANXIETY = "Anxiety"
    DEPRESSION = "Depression"
    PTSD = "PTSD"
    GRIEF = "Grief"
    SELF_ESTEEM = "Self-esteem"
    BODY_IMAGE = "Body Image"
    BIPOLAR = "Bipolar"
    WOMENS_ISSUES = "Womens Issues"
    DIVORCE_SEPARATION = "Divorce/Separation"
    BPD = "BPD"
    ADHD = "ADHD"
    LGBTQIA = "LGBTQIA+"
    EATING_DISORDERS = "Eating Disorders"
    MENS_ISSUES = "Mens Issues"
    OCD = "OCD"
    ABUSE_DV = "Abuse/DV"
    SELF_HARM = "Self-harm"
    SUBSTANCE_ABUSE_ADDICTION = "Substance Abuse/Addiction"
    ASD = "ASD"
    SUICIDAL_IDEATION = "Suicidal Ideation"

class ClinicianData:
    _instance = None
    _clinicians = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def load_clinicians(self) -> List[Dict]:
        if self._clinicians is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(script_dir, 'clinicians.json')
            try:
                with open(json_path, 'r') as file:
                    self._clinicians = json.load(file)
            except FileNotFoundError:
                print(f"Error: clinicians.json file not found at {json_path}")
                self._clinicians = []
            except json.JSONDecodeError:
                print(f"Error: clinicians.json file contains invalid JSON")
                self._clinicians = []
        return self._clinicians

    def find_clinicians_by_criteria(
        self,
        offices: Optional[List[Offices]] = None,
        groups: Optional[List[Groups]] = None,
        modalities: Optional[List[Modalities]] = None,
        specialties: Optional[List[Specialties]] = None
    ) -> List[Dict]:
        clinicians = self.load_clinicians()
        results = []
        for clinician in clinicians:
            if self._matches_criteria(clinician, 'offices', offices) and \
               self._matches_criteria(clinician, 'groups', groups) and \
               self._matches_criteria(clinician, 'modalities', modalities) and \
               self._matches_criteria(clinician, 'specialties', specialties):
                results.append(clinician)
        return results

    def _matches_criteria(self, clinician: Dict, field: str, criteria: Optional[List[Enum]]) -> bool:
        if criteria is None:
            return True
        if field not in clinician:
            return False
        return any(criterion.value in clinician[field] for criterion in criteria)

# Create a global instance of ClinicianData
clinician_data = ClinicianData.get_instance()