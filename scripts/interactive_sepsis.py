def interactive_sepsis_score(
    heart_rate, systolic_bp, map_val, resp_rate, temp, spo2,
    wbc, lactate, creatinine, bilirubin, platelets, mental_status
):
    score = 0
    if heart_rate > 100:
        score += 1
    if systolic_bp < 90 or map_val < 65:
        score += 2
    if resp_rate > 22 or resp_rate < 10:
        score += 1
    if temp > 38 or temp < 36:
        score += 1
    if spo2 < 92:
        score += 1
    if wbc > 12 or wbc < 4:
        score += 1
    if lactate > 2:
        score += 2
    if creatinine > 1.5:
        score += 1
    if bilirubin > 2:
        score += 1
    if platelets < 100:
        score += 1
    if mental_status.lower() == "y":
        score += 1

    if score >= 6:
        status = "🚨 HIGH RISK: Possible severe sepsis or septic shock."
        actions = [
            "Activate sepsis protocol.",
            "Notify physician or rapid response team immediately.",
            "Reassess vital signs and monitor patient closely.",
            "Prepare for possible fluid resuscitation and antibiotics per order."
        ]
    elif score >= 3:
        status = "⚠️ MODERATE RISK: Early indicators of sepsis detected."
        actions = [
            "Escalate findings to physician or charge nurse.",
            "Prepare to collect blood cultures, lactate, and other labs as ordered.",
            "Continue frequent monitoring of vital signs and mental status."
        ]
    else:
        status = "✅ LOW RISK: No current evidence of sepsis."
        actions = [
            "Continue routine monitoring and reassess if patient condition changes."]

    return score, status, actions
