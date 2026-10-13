import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

def swing_plan(beamCm, perSwingCm):
    if not (beamCm > 0) or not (perSwingCm > 0):
        return {"error": "the beam and the labeled swing bay must be positive"}
    if beamCm < perSwingCm:
        return {"error": "the beam is shorter than one labeled swing bay"}
    swings = math.floor(beamCm / perSwingCm)
    leftover = round1(beamCm - swings * perSwingCm)
    if swings == 1: verdict = "a solo swing"
    elif swings == 2: verdict = "a classic pair"
    else: verdict = "a full lineup"
    return {"swings": swings, "leftover": leftover, "verdict": verdict}

def clearance_plan(heightCm, ratioX):
    if not (heightCm > 0) or not (ratioX > 0):
        return {"error": "the hang height and the labeled ratio must be positive"}
    clearance = round1(heightCm * ratioX)
    if clearance < 250: verdict = "a compact zone"
    elif clearance <= 450: verdict = "a working zone"
    else: verdict = "a generous zone"
    return {"clearance": clearance, "verdict": verdict}

def chain_plan(barCm, seatCm):
    if not (barCm > 0) or not (seatCm > 0):
        return {"error": "the bar height and the seat height must be positive"}
    if seatCm >= barCm:
        return {"error": "the seat hangs at or above the bar"}
    chain = round1(barCm - seatCm)
    total = round1(2 * chain)
    if chain < 80: verdict = "a short hang"
    elif chain <= 150: verdict = "a mid hang"
    else: verdict = "a long hang"
    return {"chain": chain, "total": total, "verdict": verdict}

def render_swing(r, beamCm, perSwingCm):
    return ("A beam " + fmt(beamCm) + " cm at a labeled " + fmt(perSwingCm) + " cm bay hangs "
            + plural(r["swings"], "swing") + " with " + fmt(r["leftover"]) + " cm left at the far end - " + r["verdict"] + ".")

def render_clearance(r, heightCm, ratioX):
    return ("A hang height " + fmt(heightCm) + " cm at a labeled " + fmt(ratioX) + "x ratio asks " + fmt(r["clearance"])
            + " cm of clearance in front and the same behind - " + r["verdict"] + ".")

def render_chain(r, barCm, seatCm):
    return ("A bar " + fmt(barCm) + " cm with the seat at " + fmt(seatCm) + " cm takes " + fmt(r["chain"])
            + " cm of chain a side, " + fmt(r["total"]) + " cm in all - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[400,120],[120,120],[240,120],[600,120],[0,120],[400,0],[100,120],[365.5,120],[480,130],[200,90]]:
    add("swingPlan", swing_plan, render_swing, a)
for a in [[210,2],[100,2],[300,2],[240,1.5],[0,2],[210,0],[120,2],[180.5,2],[225,2],[500,2]]:
    add("clearancePlan", clearance_plan, render_clearance, a)
for a in [[210,40],[180,120],[240,60],[200,200],[0,40],[210,0],[220,220],[150,90],[300,75],[195.5,45.5]]:
    add("chainPlan", chain_plan, render_chain, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
