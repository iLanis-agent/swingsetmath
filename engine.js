(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function swingPlan(beamCm, perSwingCm) {
    if (!(beamCm > 0) || !(perSwingCm > 0)) return { error: "the beam and the labeled swing bay must be positive" };
    if (beamCm < perSwingCm) return { error: "the beam is shorter than one labeled swing bay" };
    var swings = Math.floor(beamCm / perSwingCm);
    var leftover = round1(beamCm - swings * perSwingCm);
    var verdict;
    if (swings === 1) verdict = "a solo swing";
    else if (swings === 2) verdict = "a classic pair";
    else verdict = "a full lineup";
    return { swings: swings, leftover: leftover, verdict: verdict };
  }

  function clearancePlan(heightCm, ratioX) {
    if (!(heightCm > 0) || !(ratioX > 0)) return { error: "the hang height and the labeled ratio must be positive" };
    var clearance = round1(heightCm * ratioX);
    var verdict;
    if (clearance < 250) verdict = "a compact zone";
    else if (clearance <= 450) verdict = "a working zone";
    else verdict = "a generous zone";
    return { clearance: clearance, verdict: verdict };
  }

  function chainPlan(barCm, seatCm) {
    if (!(barCm > 0) || !(seatCm > 0)) return { error: "the bar height and the seat height must be positive" };
    if (seatCm >= barCm) return { error: "the seat hangs at or above the bar" };
    var chain = round1(barCm - seatCm);
    var total = round1(2 * chain);
    var verdict;
    if (chain < 80) verdict = "a short hang";
    else if (chain <= 150) verdict = "a mid hang";
    else verdict = "a long hang";
    return { chain: chain, total: total, verdict: verdict };
  }

  function renderSwing(r, beamCm, perSwingCm) {
    return "A beam " + beamCm + " cm at a labeled " + perSwingCm + " cm bay hangs " + plural(r.swings, "swing") + " with " + r.leftover + " cm left at the far end - " + r.verdict + ".";
  }

  function renderClearance(r, heightCm, ratioX) {
    return "A hang height " + heightCm + " cm at a labeled " + ratioX + "x ratio asks " + r.clearance + " cm of clearance in front and the same behind - " + r.verdict + ".";
  }

  function renderChain(r, barCm, seatCm) {
    return "A bar " + barCm + " cm with the seat at " + seatCm + " cm takes " + r.chain + " cm of chain a side, " + r.total + " cm in all - " + r.verdict + ".";
  }

  var api = { swingPlan: swingPlan, clearancePlan: clearancePlan, chainPlan: chainPlan, renderSwing: renderSwing, renderClearance: renderClearance, renderChain: renderChain };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.SwingsetMath = api;
})(this);
