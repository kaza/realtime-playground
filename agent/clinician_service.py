from clinician_data import Offices, Groups, Modalities, Specialties, clinician_data
from typing import Optional, Union, List

def get_clinician_info(
    offices: Optional[Union[str, List[str]]] = None,
    groups: Optional[Union[str, List[str]]] = None,
    modalities: Optional[Union[str, List[str]]] = None,
    specialties: Optional[Union[str, List[str]]] = None
) -> str:
    def to_enums(enum_class, input_data):
        if input_data is None:
            return None
        if isinstance(input_data, str):
            input_list = [item.strip() for item in input_data.split(',') if item.strip()]
        elif isinstance(input_data, list):
            input_list = input_data
        else:
            raise ValueError(f"Invalid input type for {enum_class.__name__}: {type(input_data)}")
        
        valid_enums = []
        for item in input_list:
            try:
                enum_value = enum_class(item)
                valid_enums.append(enum_value)
            except ValueError:
                print(f"Warning: '{item}' is not a valid {enum_class.__name__}. Skipping this value.")
        return valid_enums if valid_enums else None

    office_enums = to_enums(Offices, offices)
    group_enums = to_enums(Groups, groups)
    modality_enums = to_enums(Modalities, modalities)
    specialty_enums = to_enums(Specialties, specialties)

    clinicians = clinician_data.find_clinicians_by_criteria(office_enums, group_enums, modality_enums, specialty_enums)

    if not clinicians:
        return "No clinicians found matching the specified criteria."

    results = []
    for clinician in clinicians:
        info = f"Name: {clinician['name']}\n"
        info += f"Offices: {', '.join(clinician['office'])}\n"
        info += f"Groups: {', '.join(clinician['groups'])}\n"
        info += f"Modalities: {', '.join(clinician['modalities'])}\n"
        info += f"Specialties: {', '.join(clinician['specialties'])}\n"
        results.append(info)

    return "\n\n".join(results)