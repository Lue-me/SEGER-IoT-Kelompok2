"""
SEGER - Model Decision Tree (dibuat otomatis oleh ai/train_model.py)

Fitur: temp (C), hum (%), co2 (ppm)
Kelas: MULAI PENGAP, NYAMAN, PENGAP
"""


def predict_ai(temp, hum, co2):
    """Return label kondisi ruangan hasil prediksi Decision Tree."""
    if co2 <= 1101.5:
        if co2 <= 695.5:
            if temp <= 30.55:
                return 'NYAMAN'
            else:
                if co2 <= 603.0:
                    return 'NYAMAN'
                else:
                    return 'MULAI PENGAP'
        else:
            if temp <= 31.35:
                return 'MULAI PENGAP'
            else:
                if co2 <= 877.5:
                    return 'MULAI PENGAP'
                else:
                    return 'PENGAP'
    else:
        if co2 <= 1220.5:
            if temp <= 28.3:
                if hum <= 70.4:
                    return 'MULAI PENGAP'
                else:
                    return 'PENGAP'
            else:
                return 'PENGAP'
        else:
            return 'PENGAP'
