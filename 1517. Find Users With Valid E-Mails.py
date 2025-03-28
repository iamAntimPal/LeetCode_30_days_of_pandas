def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[
        patients['conditions'].str.contains(r'(^DIAB1)|( DIAB1)')
    ]