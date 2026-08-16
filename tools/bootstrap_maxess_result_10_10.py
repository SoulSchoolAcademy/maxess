from pathlib import Path
import re

ARTIFACTS = [
    "MAXESS-RESULTS-FINAL-GROOVE.html",
    "MAXESS-RESULTS-FINAL-GROOVE-EMBED.html",
    "MAXESS-RESULTS-10-GROOVE.html",
    "MAXESS-RESULTS-GROOVE-EMBED.html",
    "MAXESS-RESULTS-GROOVE-EMBED-9.95.html",
]

MARKER = "MAXESS_RESULT_10_10_BOOTSTRAP"

BOOTSTRAP = '''<!-- MAXESS_RESULT_10_10_BOOTSTRAP -->
<script>
(function () {
  "use strict";

  /* MAXESS_RESULT exists before ANY visual layer executes.
     A real cross-domain ?result= payload always wins.
     The 10.10 object is only the deterministic development fallback. */
  var result = null;

  try {
    var encoded = new URLSearchParams(window.location.search).get("result");
    if (encoded) {
      var normalized = encoded.replace(/-/g, "+").replace(/_/g, "/");
      while (normalized.length % 4) normalized += "=";
      var binary = atob(normalized);
      var bytes = new Uint8Array(binary.length);
      for (var i = 0; i < binary.length; i++) {
        bytes[i] = binary.charCodeAt(i);
      }
      result = JSON.parse(new TextDecoder().decode(bytes));
    }
  } catch (error) {
    console.warn("MAXESS_RESULT query payload could not be decoded; using bootstrap fallback.", error);
  }

  window.MAXESS_RESULT = result || {
    resonance: 10.10,
    signature: "LIVING",
    naya: "AWAKENED",
    groove: "MAXIMAL",
    status: "FULL_ACTIVATION",
    timestamp: new Date().toISOString()
  };

  console.log(
    "%cMAXESS 10.10 INITIALIZED",
    "color:#00ffcc; font-size:18px; font-weight:bold;"
  );
})();
</script>
'''

changed = 0
for filename in ARTIFACTS:
    path = Path(filename)
    if not path.exists():
        print(f"SKIP: {filename} does not exist")
        continue

    source = path.read_text(encoding="utf-8")
    if MARKER in source:
        print(f"PASS: {filename} already contains {MARKER}")
        continue

    match = re.search(r"<head(?:\s[^>]*)?>", source, flags=re.I)
    if not match:
        raise SystemExit(f"FAIL: {filename} has no <head> element")

    patched = source[:match.end()] + "\n" + BOOTSTRAP + source[match.end():]
    path.write_text(patched, encoding="utf-8")
    changed += 1
    print(f"INJECTED: {filename}")

if changed == 0:
    print("No artifact required a new bootstrap injection.")
