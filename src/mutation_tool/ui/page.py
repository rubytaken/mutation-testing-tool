# ruff: noqa: E501

INDEX_HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mutation Lab</title>
  <style>
    :root {
      --paper: #f4efe6;
      --ink: #12222b;
      --card: rgba(255, 250, 242, 0.82);
      --line: rgba(18, 34, 43, 0.12);
      --accent: #d9713c;
      --accent-2: #177e89;
      --accent-3: #f0c36a;
      --danger: #aa3f2a;
      --success: #1b7f5d;
      --muted: #53656d;
      --shadow: 0 24px 60px rgba(18, 34, 43, 0.12);
      --shadow-soft: 0 12px 30px rgba(18, 34, 43, 0.08);
      --radius: 22px;
    }

    * { box-sizing: border-box; }

    html { scroll-behavior: smooth; }

    body {
      margin: 0;
      min-height: 100vh;
      font-family: Aptos, Candara, "Trebuchet MS", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(217, 113, 60, 0.24), transparent 28%),
        radial-gradient(circle at top right, rgba(23, 126, 137, 0.20), transparent 24%),
        linear-gradient(180deg, #fcf7ef 0%, #f4efe6 48%, #efe6d9 100%);
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background-image: linear-gradient(rgba(18, 34, 43, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(18, 34, 43, 0.03) 1px, transparent 1px);
      background-size: 42px 42px;
      mask-image: linear-gradient(180deg, rgba(0, 0, 0, 0.35), transparent 75%);
    }

    .shell {
      width: min(1260px, calc(100% - 32px));
      margin: 28px auto 48px;
      position: relative;
      z-index: 1;
    }

    .hero,
    .panel,
    .tour-card {
      background: var(--card);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(255, 255, 255, 0.45);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }

    .hero {
      padding: 28px;
      margin-bottom: 18px;
      display: grid;
      gap: 16px;
      animation: rise 0.45s ease-out;
    }

    .hero-top {
      display: flex;
      justify-content: space-between;
      align-items: start;
      gap: 14px;
    }

    .lang-toggle {
      display: inline-flex;
      gap: 8px;
      padding: 6px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.64);
      border: 1px solid rgba(18, 34, 43, 0.08);
    }

    .lang-button {
      min-width: 56px;
      padding: 8px 12px;
      border-radius: 999px;
      box-shadow: none;
    }

    .lang-button.active {
      background: linear-gradient(135deg, var(--accent-2), #11676f);
      color: white;
    }

    .eyebrow {
      text-transform: uppercase;
      letter-spacing: 0.18em;
      font-size: 0.76rem;
      color: var(--accent-2);
      font-weight: 700;
    }

    h1, h2, h3 {
      margin: 0;
      font-family: Cambria, Georgia, serif;
      font-weight: 700;
      letter-spacing: -0.03em;
    }

    h1 {
      font-size: clamp(2.3rem, 6vw, 4.2rem);
      line-height: 0.95;
      max-width: 11ch;
    }

    .hero-copy {
      max-width: 72ch;
      color: var(--muted);
      font-size: 1rem;
      line-height: 1.6;
    }

    .pill-row,
    .hero-actions,
    .button-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .pill {
      padding: 9px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.62);
      border: 1px solid rgba(18, 34, 43, 0.08);
      font-size: 0.92rem;
    }

    .tour-grid,
    .guide-grid,
    .reference-grid {
      display: grid;
      gap: 18px;
      margin-bottom: 18px;
    }

    .tour-grid {
      grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .guide-grid,
    .reference-grid {
      grid-template-columns: minmax(0, 1.18fr) minmax(0, 0.82fr);
    }

    .tour-card {
      padding: 22px;
      animation: rise 0.55s ease-out;
    }

    .tour-number,
    .step-number {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 34px;
      height: 34px;
      border-radius: 999px;
      background: rgba(217, 113, 60, 0.16);
      color: #8d421a;
      font-weight: 800;
      margin-bottom: 12px;
    }

    .grid {
      display: grid;
      grid-template-columns: minmax(330px, 430px) minmax(0, 1fr);
      gap: 18px;
      margin-bottom: 18px;
    }

    .panel {
      padding: 22px;
      animation: rise 0.55s ease-out;
    }

    .panel + .panel {
      animation-delay: 0.05s;
    }

    .panel-header {
      display: flex;
      justify-content: space-between;
      align-items: start;
      gap: 14px;
      margin-bottom: 18px;
    }

    .panel-copy {
      margin: 6px 0 0;
      color: var(--muted);
      line-height: 1.55;
      font-size: 0.95rem;
    }

    .stack,
    .step-grid,
    .legend-grid,
    .request-grid {
      display: grid;
      gap: 14px;
    }

    .step-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      margin-top: 16px;
    }

    .step-card,
    .legend-card,
    .code-card {
      border-radius: 18px;
      padding: 14px;
      background: rgba(255, 255, 255, 0.68);
      border: 1px solid rgba(18, 34, 43, 0.08);
      box-shadow: var(--shadow-soft);
    }

    .request-grid {
      margin-top: 16px;
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .legend-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      margin-top: 16px;
    }

    label {
      display: grid;
      gap: 8px;
      font-size: 0.92rem;
      font-weight: 700;
    }

    input,
    textarea,
    select {
      width: 100%;
      border-radius: 16px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.74);
      color: var(--ink);
      padding: 12px 14px;
      font: inherit;
      transition: border-color 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease;
    }

    input:focus,
    textarea:focus,
    select:focus {
      outline: none;
      border-color: rgba(23, 126, 137, 0.55);
      box-shadow: 0 0 0 4px rgba(23, 126, 137, 0.12);
      transform: translateY(-1px);
    }

    select[multiple] {
      min-height: 140px;
    }

    .field-help,
    .mini-note {
      color: var(--muted);
      font-size: 0.88rem;
      line-height: 1.55;
      font-weight: 500;
    }

    .mini-note {
      font-size: 0.82rem;
      display: block;
    }

    .split {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }

    .checkbox {
      display: flex;
      align-items: start;
      gap: 10px;
      font-weight: 700;
    }

    .checkbox input {
      width: 18px;
      height: 18px;
      padding: 0;
      margin-top: 2px;
    }

    button {
      appearance: none;
      border: 0;
      border-radius: 999px;
      padding: 12px 18px;
      font: inherit;
      font-weight: 800;
      letter-spacing: 0.02em;
      cursor: pointer;
      transition: transform 0.18s ease, box-shadow 0.18s ease, opacity 0.18s ease;
    }

    button:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 26px rgba(18, 34, 43, 0.16);
    }

    .primary {
      background: linear-gradient(135deg, var(--accent), #c9562b);
      color: white;
    }

    .ghost {
      background: rgba(255, 255, 255, 0.72);
      color: var(--ink);
      border: 1px solid var(--line);
    }

    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border-radius: 999px;
      padding: 8px 12px;
      font-size: 0.88rem;
      font-weight: 800;
      background: rgba(255, 255, 255, 0.74);
      border: 1px solid var(--line);
    }

    .status-badge::before {
      content: "";
      width: 9px;
      height: 9px;
      border-radius: 999px;
      background: var(--muted);
    }

    .status-idle::before { background: #7f8f96; }
    .status-running::before { background: var(--accent); box-shadow: 0 0 0 8px rgba(217, 113, 60, 0.14); }
    .status-completed::before { background: var(--success); }
    .status-failed::before { background: var(--danger); }

    .metric-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      margin-top: 14px;
    }

    .metric {
      border-radius: 18px;
      padding: 14px;
      background: rgba(255, 255, 255, 0.68);
      border: 1px solid rgba(18, 34, 43, 0.08);
    }

    .metric-label {
      color: var(--muted);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }

    .metric-value {
      margin-top: 6px;
      font-size: 1.9rem;
      font-weight: 800;
    }

    .info-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
      margin-top: 16px;
    }

    .info-card {
      border-radius: 18px;
      padding: 14px;
      background: rgba(255, 255, 255, 0.68);
      border: 1px solid rgba(18, 34, 43, 0.08);
      min-height: 94px;
    }

    .info-key {
      display: block;
      color: var(--muted);
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      margin-bottom: 8px;
    }

    .results {
      margin-top: 18px;
    }

    .callout {
      border-radius: 18px;
      padding: 16px;
      background: rgba(255, 255, 255, 0.72);
      border: 1px solid rgba(18, 34, 43, 0.08);
      margin-top: 14px;
    }

    .summary-callout {
      border-left: 5px solid var(--accent);
    }

    .guidance-callout {
      border-left: 5px solid var(--accent-2);
    }

    .details {
      margin-top: 12px;
      display: grid;
      gap: 10px;
    }

    details {
      border-radius: 16px;
      padding: 12px 14px;
      background: rgba(18, 34, 43, 0.04);
    }

    details summary {
      cursor: pointer;
      font-weight: 700;
    }

    pre {
      margin: 12px 0 0;
      white-space: pre-wrap;
      word-break: break-word;
      font-family: Consolas, "Courier New", monospace;
      font-size: 0.86rem;
      color: #17303b;
    }

    code,
    .inline-code {
      font-family: Consolas, "Courier New", monospace;
      font-size: 0.92em;
    }

    .table-wrap {
      margin-top: 14px;
      overflow: auto;
      border-radius: 18px;
      border: 1px solid rgba(18, 34, 43, 0.08);
      background: rgba(255, 255, 255, 0.72);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      min-width: 820px;
    }

    th,
    td {
      text-align: left;
      padding: 12px 14px;
      border-bottom: 1px solid rgba(18, 34, 43, 0.08);
      vertical-align: top;
      font-size: 0.93rem;
    }

    th {
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--muted);
      background: rgba(18, 34, 43, 0.04);
    }

    .chip {
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      padding: 5px 10px;
      font-size: 0.77rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      background: rgba(18, 34, 43, 0.08);
    }

    .chip-killed { background: rgba(27, 127, 93, 0.16); color: #155540; }
    .chip-survived { background: rgba(217, 113, 60, 0.18); color: #8d421a; }
    .chip-timeout { background: rgba(23, 126, 137, 0.16); color: #115b62; }
    .chip-error { background: rgba(170, 63, 42, 0.16); color: #7a2b1d; }

    .hint {
      color: var(--muted);
      font-size: 0.88rem;
      line-height: 1.55;
    }

    .muted { color: var(--muted); }

    .empty {
      padding: 22px;
      text-align: center;
      color: var(--muted);
    }

    ul {
      margin: 10px 0 0;
      padding-left: 18px;
    }

    li + li {
      margin-top: 6px;
    }

    #usage-guide {
      scroll-margin-top: 24px;
    }

    @keyframes rise {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 980px) {
      .tour-grid,
      .grid,
      .guide-grid,
      .reference-grid,
      .metric-grid,
      .info-grid,
      .split,
      .step-grid,
      .request-grid,
      .legend-grid {
        grid-template-columns: 1fr;
      }

      .shell {
        width: min(100% - 20px, 1260px);
      }
    }

    @media (max-width: 720px) {
      .hero-top {
        flex-direction: column;
        align-items: stretch;
      }

      .lang-toggle {
        align-self: flex-end;
      }
    }
  </style>
</head>
<body>
  <div class="shell">
    <section class="hero">
      <div class="hero-top">
        <div class="eyebrow">Local Mutation Dashboard</div>
        <div class="lang-toggle" aria-label="Language switcher">
          <button class="ghost lang-button" type="button" id="lang-en-button">EN</button>
          <button class="ghost lang-button" type="button" id="lang-tr-button">TR</button>
        </div>
      </div>
      <h1>Mutation Lab</h1>
      <p class="hero-copy">
        Run mutation analysis without leaving the browser. This page is both the control center
        and the onboarding guide: launch a session, watch the baseline, inspect survivors, and
        learn how to turn them into stronger tests.
      </p>
      <div class="pill-row">
        <div class="pill">Baseline test run comes first</div>
        <div class="pill">Mutants are generated from the AST</div>
        <div class="pill">Detailed usage guide included</div>
        <div class="pill">JSON report is preserved</div>
      </div>
      <label>
        Choose a demo
        <select id="demo-select" aria-label="Choose a demo">
          <option value="beginner" data-tr-label="Başlangıç Demosu">Beginner Demo</option>
          <option value="ci_gate" data-tr-label="CI Geçit Demosu">CI Gate Demo</option>
          <option value="timeout_lab" data-tr-label="Timeout Laboratuvarı Demosu">Timeout Lab Demo</option>
        </select>
        <span class="field-help" id="demo-summary">
          Beginner Demo introduces a weak boundary assertion so you can inspect a survivor on your first pass.
        </span>
        <span class="field-help" id="demo-goal">
          Learning goal: inspect a survivor and turn it into one focused test.
        </span>
      </label>
      <div class="hero-actions">
        <button class="primary" type="button" id="starter-button">Use Starter Settings</button>
        <button class="ghost" type="button" id="demo-button">Load Selected Demo</button>
        <button class="ghost" type="button" id="demo-run-button">Run Selected Demo</button>
        <button class="ghost" type="button" id="guide-button">Open Usage Guide</button>
      </div>
      <p class="mini-note" id="demo-inline-note">
        Load Selected Demo fills the form with the active demo settings. Run Selected Demo fills those
        values and starts the example immediately. After the run, use Download Latest Report or
        Download Latest PDF to save the results.
      </p>
    </section>

    <section class="tour-grid">
      <article class="tour-card">
        <div class="tour-number">1</div>
        <h3>Start Small</h3>
        <p class="panel-copy">
          Begin with one package or a batch of 10 mutants. Smaller runs make it easier to
          understand why a mutant survived.
        </p>
      </article>
      <article class="tour-card">
        <div class="tour-number">2</div>
        <h3>Read the Changed Behavior</h3>
        <p class="panel-copy">
          A survivor means the tests still passed after behavior changed. The change itself is the
          clue for the next test you should write.
        </p>
      </article>
      <article class="tour-card">
        <div class="tour-number">3</div>
        <h3>Improve and Rerun</h3>
        <p class="panel-copy">
          Add one focused assertion for the missing behavior, rerun the same scope, then widen the
          run when the weak spot is closed.
        </p>
      </article>
    </section>

    <div class="grid">
      <section class="panel">
        <div class="panel-header">
          <div>
            <h2>Run Setup</h2>
            <p class="panel-copy">Choose a project, narrow the scope, and start the next mutation pass.</p>
          </div>
        </div>

        <form id="run-form" class="stack">
          <label>
            Project root
            <input id="project-root" name="project_root" value="." required>
            <span class="field-help">
              The folder of the project you want to analyze. In most cases use
              <span class="inline-code">.</span> when the terminal is already inside that project.
            </span>
          </label>

          <label>
            Config path
            <input id="config-path" name="config_path" placeholder="Optional pyproject.toml path">
            <span class="field-help">
              Leave blank to use <span class="inline-code">pyproject.toml</span> from the project root.
            </span>
          </label>

          <label>
            Source paths
            <input id="source-paths" name="source_paths" placeholder="src, package/module.py">
            <span class="field-help">
              Comma-separated paths to mutate. Recommended first value:
              <span class="inline-code">src</span>.
            </span>
          </label>

          <label>
            Operators
            <select id="operators" name="operators" multiple></select>
            <span class="field-help">
              Leave all operators unselected to run the full default set. Select a subset only when
              you want a focused pass.
            </span>
          </label>

          <div class="split">
            <label>
              Max mutants
              <input id="max-mutants" name="max_mutants" type="number" min="1" placeholder="Optional">
              <span class="field-help">Use 5-20 for an easy first run.</span>
            </label>

            <label>
              Timeout (sec)
              <input id="timeout" name="per_mutant_timeout" type="number" min="0.1" step="0.1" placeholder="Optional">
              <span class="field-help">Leave blank to auto-calculate from the baseline run.</span>
            </label>
          </div>

          <label class="checkbox">
            <input id="stop-on-survivor" type="checkbox">
            <span>
              Stop after the first survivor
              <span class="mini-note">Best for fast local feedback when you only need the first actionable gap.</span>
            </span>
          </label>

          <label class="checkbox">
            <input id="fail-on-survivor" type="checkbox">
            <span>
              Fail run when a survivor appears
              <span class="mini-note">Best for CI or quality gates where any survivor should fail the run.</span>
            </span>
          </label>

          <div class="button-row">
            <button class="primary" type="submit">Start Mutation Run</button>
            <button class="ghost" type="button" id="form-demo-button">Load Selected Demo</button>
            <button class="ghost" type="button" id="reset-button">Reset Form</button>
            <button class="ghost" type="button" id="refresh-button">Refresh Status</button>
          </div>
        </form>
      </section>

      <section class="panel">
        <div class="panel-header">
          <div>
            <h2>Control Room</h2>
            <p class="panel-copy">Track the current state, the latest report path, and the headline mutation metrics here.</p>
          </div>
          <div id="status-badge" class="status-badge status-idle">Idle</div>
        </div>

        <p id="status-message" class="hint">Ready to launch mutation analysis.</p>

        <div class="info-grid">
          <div class="info-card">
            <span class="info-key">Started</span>
            <div id="started-at" class="muted">-</div>
          </div>
          <div class="info-card">
            <span class="info-key">Finished</span>
            <div id="finished-at" class="muted">-</div>
          </div>
          <div class="info-card">
            <span class="info-key">Report</span>
            <div id="report-path" class="muted">-</div>
          </div>
        </div>

        <div class="metric-grid">
          <div class="metric">
            <div class="metric-label">Score</div>
            <div class="metric-value" id="score-value">0%</div>
          </div>
          <div class="metric">
            <div class="metric-label">Killed</div>
            <div class="metric-value" id="killed-value">0</div>
          </div>
          <div class="metric">
            <div class="metric-label">Survived</div>
            <div class="metric-value" id="survived-value">0</div>
          </div>
          <div class="metric">
            <div class="metric-label">Executed</div>
            <div class="metric-value" id="executed-value">0</div>
          </div>
          <div class="metric">
            <div class="metric-label">Generated</div>
            <div class="metric-value" id="generated-value">0</div>
          </div>
          <div class="metric">
            <div class="metric-label">Files</div>
            <div class="metric-value" id="discovered-value">0</div>
          </div>
        </div>

        <div id="request-hint" class="request-grid"></div>
        <div class="button-row">
          <button class="ghost" type="button" id="download-report-button">Download Latest Report</button>
          <button class="ghost" type="button" id="download-pdf-button">Download Latest PDF</button>
        </div>
      </section>
    </div>

    <div class="guide-grid">
      <section class="panel" id="usage-guide">
        <div class="panel-header">
          <div>
            <h2>How To Use Mutation Lab</h2>
            <p class="panel-copy">
              This guide is designed for both first-time users and teams turning mutation testing into
              a regular workflow.
            </p>
          </div>
        </div>

        <div class="step-grid">
          <article class="step-card">
            <div class="step-number">1</div>
            <h3>Confirm the normal test suite is green</h3>
            <p class="panel-copy">
              Mutation testing only makes sense after the regular test suite passes. If the baseline
              fails, fix that first and try again.
            </p>
          </article>
          <article class="step-card">
            <div class="step-number">2</div>
            <h3>Choose a small scope</h3>
            <p class="panel-copy">
              Start with <span class="inline-code">src</span> and around 10 mutants. That keeps the output readable
              and makes the first run much easier to learn from.
            </p>
          </article>
          <article class="step-card">
            <div class="step-number">3</div>
            <h3>Inspect survivors carefully</h3>
            <p class="panel-copy">
              A surviving mutant means tests still passed after the behavior changed. That usually
              means an edge case, branch, or assertion is missing.
            </p>
          </article>
          <article class="step-card">
            <div class="step-number">4</div>
            <h3>Add one focused test and rerun</h3>
            <p class="panel-copy">
              Read the original and mutated snippets, identify the changed expectation, write one
              targeted test, and rerun the same scope.
            </p>
          </article>
        </div>

        <div class="details">
          <details open>
            <summary>Recommended first run</summary>
            <p class="panel-copy">
              If you are new to mutation testing, start with these values:
              project root <span class="inline-code">.</span>, source paths <span class="inline-code">src</span>,
              max mutants <span class="inline-code">10</span>, leave timeout blank, and keep both survivor
              checkboxes off.
            </p>
          </details>

          <details>
            <summary>How do I use the demo catalog?</summary>
            <p class="panel-copy">
              Choose a demo first, then click <span class="inline-code">Load Selected Demo</span> to fill the form
              with that scenario. Review the values if you want to learn what each field means, then click
              <span class="inline-code">Start Mutation Run</span>. Use
              <span class="inline-code">Run Selected Demo</span> when you want one-click fill + run.
              After the run, keep the JSON report for tooling and download the PDF when you want a human-readable summary.
            </p>
          </details>

          <details>
            <summary>What should you do after a survivor?</summary>
            <p class="panel-copy">
              Example: if the tool shows <span class="inline-code">value &gt; 0 -&gt; value &gt;= 0</span> and
              that mutant survives, your tests probably never prove what should happen for
              <span class="inline-code">0</span>. Add a test for that exact boundary and rerun.
            </p>
          </details>
        </div>

        <div class="code-card">
          <span class="info-key">Starter pyproject.toml</span>
          <pre>[tool.mutation_tool]
source_paths = ["src"]
test_command = ["pytest", "-q"]
exclude = ["tests/**", "**/__pycache__/**"]
timeout_multiplier = 5.0
min_timeout = 5.0</pre>
        </div>
      </section>

      <section class="panel">
        <div class="panel-header">
          <div>
            <h2>Field Guide</h2>
            <p class="panel-copy">
              Use this as a quick reference for what belongs in each form field.
            </p>
          </div>
        </div>

        <div class="details">
          <details open>
            <summary>Project root</summary>
            <p class="panel-copy">
              The project folder you want to analyze. If the terminal is already in that folder, use
              <span class="inline-code">.</span>.
            </p>
          </details>
          <details>
            <summary>Config path</summary>
            <p class="panel-copy">
              Use this only if you want to point at a specific config file. In most cases leave it
              blank and let the tool load <span class="inline-code">pyproject.toml</span> automatically.
            </p>
          </details>
          <details>
            <summary>Source paths</summary>
            <p class="panel-copy">
              Comma-separated paths to mutate. Good examples are
              <span class="inline-code">src</span>, <span class="inline-code">src/my_package</span>, or
              <span class="inline-code">src/my_package/service.py</span>.
            </p>
          </details>
          <details>
            <summary>Operators</summary>
            <p class="panel-copy">
              Leave everything unselected to run all default operators. Choose a subset only when
              you want a specific kind of mutation pass.
            </p>
          </details>
          <details>
            <summary>Max mutants and timeout</summary>
            <p class="panel-copy">
              While learning, 5-20 mutants is a good range. Leave timeout blank unless your test suite
              genuinely needs a manual budget.
            </p>
          </details>
          <details>
            <summary>Stop on survivor vs fail on survivor</summary>
            <p class="panel-copy">
              Stop on survivor is for fast local learning. Fail on survivor is for CI or stricter
              quality gates where even one survivor should fail the run.
            </p>
          </details>
        </div>
      </section>
    </div>

    <div class="reference-grid">
      <section class="panel">
        <div class="panel-header">
          <div>
            <h2>Result Legend</h2>
            <p class="panel-copy">
              These are the outcomes you will see in the results table.
            </p>
          </div>
        </div>

        <div class="legend-grid">
          <article class="legend-card">
            <span class="chip chip-killed">killed</span>
            <p class="panel-copy">Tests failed after the mutation. This is good: the changed behavior was detected.</p>
          </article>
          <article class="legend-card">
            <span class="chip chip-survived">survived</span>
            <p class="panel-copy">Tests still passed after the mutation. This points to a missing assertion or edge case.</p>
          </article>
          <article class="legend-card">
            <span class="chip chip-timeout">timeout</span>
            <p class="panel-copy">The mutated run took too long. Review loops, waits, or increase the timeout budget.</p>
          </article>
          <article class="legend-card">
            <span class="chip chip-error">error</span>
            <p class="panel-copy">The mutation caused a syntax or import problem instead of a clean test failure.</p>
          </article>
        </div>
      </section>

      <section class="panel">
        <div class="panel-header">
          <div>
            <h2>CLI Equivalents</h2>
            <p class="panel-copy">
              The UI and CLI use the same engine. These commands match the common UI flows.
            </p>
          </div>
        </div>

        <div class="code-card">
          <span class="info-key">Useful commands</span>
          <pre>python -m mutation_tool list-operators
python -m mutation_tool run . --max-mutants 10
python -m mutation_tool run . --operator comparison --operator logical
python -m mutation_tool run . --stop-on-survivor
python -m mutation_tool run . --fail-on-survivor</pre>
        </div>

        <div class="code-card">
          <span class="info-key">Built-in demo</span>
          <pre>Project root: examples/beginner_demo
Source paths: src
Max mutants: 10
Timeout: leave blank</pre>
        </div>
      </section>
    </div>

    <section class="panel results">
      <div class="panel-header">
        <div>
            <h2>Results</h2>
            <p class="panel-copy">Use surviving mutants to find weak assertions and missing edge-case tests.</p>
        </div>
      </div>

      <div id="baseline-panel" class="callout">
        <strong>Baseline</strong>
        <p class="panel-copy">No run yet.</p>
      </div>

      <div id="summary-callout" class="callout summary-callout">
        <strong>Ready for your first run.</strong>
        <p class="panel-copy">
          Start with a small batch, inspect the surviving change, and turn it into a focused test.
        </p>
      </div>

      <div id="guidance-panel" class="callout guidance-callout">
        <strong>Next-step guidance will appear here.</strong>
        <p class="panel-copy">After a run, this panel summarizes what to do next.</p>
      </div>

      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Status</th>
              <th>File</th>
              <th>Line</th>
              <th>Operator</th>
              <th>Change</th>
              <th>Summary</th>
            </tr>
          </thead>
          <tbody id="mutant-body">
            <tr>
              <td colspan="6" class="empty">Start a run to see mutant details.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  </div>

  <script>
    const statusBadge = document.getElementById('status-badge');
    const statusMessage = document.getElementById('status-message');
    const startedAt = document.getElementById('started-at');
    const finishedAt = document.getElementById('finished-at');
    const reportPath = document.getElementById('report-path');
    const scoreValue = document.getElementById('score-value');
    const killedValue = document.getElementById('killed-value');
    const survivedValue = document.getElementById('survived-value');
    const executedValue = document.getElementById('executed-value');
    const generatedValue = document.getElementById('generated-value');
    const discoveredValue = document.getElementById('discovered-value');
    const mutantBody = document.getElementById('mutant-body');
    const baselinePanel = document.getElementById('baseline-panel');
    const summaryCallout = document.getElementById('summary-callout');
    const guidancePanel = document.getElementById('guidance-panel');
    const requestHint = document.getElementById('request-hint');
    const operatorSelect = document.getElementById('operators');
    const demoSelect = document.getElementById('demo-select');
    const demoSummary = document.getElementById('demo-summary');
    const demoGoal = document.getElementById('demo-goal');
    const form = document.getElementById('run-form');
    const refreshButton = document.getElementById('refresh-button');
    const demoButton = document.getElementById('demo-button');
    const demoRunButton = document.getElementById('demo-run-button');
    const formDemoButton = document.getElementById('form-demo-button');
    const starterButton = document.getElementById('starter-button');
    const resetButton = document.getElementById('reset-button');
    const guideButton = document.getElementById('guide-button');
    const downloadReportButton = document.getElementById('download-report-button');
    const downloadPdfButton = document.getElementById('download-pdf-button');
    const langEnButton = document.getElementById('lang-en-button');
    const langTrButton = document.getElementById('lang-tr-button');
    const languageStorageKey = 'mutation-lab-language';

    let demoCatalog = [
      {
        id: 'beginner',
        name: { en: 'Beginner Demo', tr: 'Başlangıç Demosu' },
        summary: {
          en: 'A friendly first run with a weak boundary assertion that produces a survivor.',
          tr: 'İlk survivor deneyimi için zayıf bir sınır assertion\'ı içeren dost canlısı demo.',
        },
        learning_goal: {
          en: 'Learn how to inspect a survivor and add a focused test.',
          tr: 'Bir survivor\'ı inceleyip hedefli bir test eklemeyi öğren.',
        },
      },
      {
        id: 'ci_gate',
        name: { en: 'CI Gate Demo', tr: 'CI Geçit Demosu' },
        summary: {
          en: 'Shows how a surviving mutant should fail a stricter quality gate.',
          tr: 'Hayatta kalan bir mutantın daha sıkı kalite kapısını nasıl fail etmesi gerektiğini gösterir.',
        },
        learning_goal: {
          en: 'Practice the difference between local exploration and CI enforcement.',
          tr: 'Yerel keşif ile CI yaptırımı arasındaki farkı deneyimle.',
        },
      },
      {
        id: 'timeout_lab',
        name: { en: 'Timeout Lab Demo', tr: 'Timeout Laboratuvarı Demosu' },
        summary: {
          en: 'Designed to surface a slow-path mutant so you can practice timeout diagnosis.',
          tr: 'Timeout tanılaması pratiği için yavaş yol mutantı üretmek üzere tasarlanmıştır.',
        },
        learning_goal: {
          en: 'Learn how timeout budgets and slow paths affect mutation results.',
          tr: 'Timeout bütçeleriyle yavaş yolların mutation sonuçlarını nasıl etkilediğini öğren.',
        },
      },
    ];
    let currentLanguage = 'en';
    let lastSnapshot = {
      status: 'idle',
      message: 'Ready to launch mutation analysis.',
      pdf_report_path: null,
      result: null,
    };

    function escapeHtml(value) {
      return String(value ?? '')
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }

    function formatTime(value) {
      if (!value) return '-';
      const date = new Date(value);
      if (Number.isNaN(date.getTime())) return value;
      return date.toLocaleString();
    }

    function languageValue(enValue, trValue) {
      return currentLanguage === 'en' ? enValue : trValue;
    }

    function setText(selector, enValue, trValue) {
      const element = document.querySelector(selector);
      if (element) {
        element.textContent = languageValue(enValue, trValue);
      }
    }

    function setHTML(selector, enValue, trValue) {
      const element = document.querySelector(selector);
      if (element) {
        element.innerHTML = languageValue(enValue, trValue);
      }
    }

    function setPlaceholder(selector, enValue, trValue) {
      const element = document.querySelector(selector);
      if (element) {
        element.setAttribute('placeholder', languageValue(enValue, trValue));
      }
    }

    function setLeadText(selector, enValue, trValue) {
      const element = document.querySelector(selector);
      if (element && element.firstChild) {
        element.firstChild.textContent = `\n            ${languageValue(enValue, trValue)}\n            `;
      }
    }

    function setNestedLeadText(selector, enValue, trValue) {
      const element = document.querySelector(selector);
      if (element && element.firstChild) {
        element.firstChild.textContent = `\n              ${languageValue(enValue, trValue)}\n              `;
      }
    }

    function localizeBackendText(text) {
      if (!text || currentLanguage === 'en') {
        return text;
      }

      const exactMatches = {
        'Ready to launch mutation analysis.': 'Mutation analizi başlatılmaya hazır.',
        'Mutation analysis is running.': 'Mutation analizi çalışıyor.',
        'Mutation analysis completed.': 'Mutation analizi tamamlandı.',
        'Mutation analysis failed.': 'Mutation analizi başarısız oldu.',
        'A mutation run is already in progress.': 'Halihazırda çalışan bir mutation koşusu var.',
        'Built-in demo project was not found.': 'Yerleşik demo projesi bulunamadı.',
        'Built-in demo could not be loaded.': 'Yerleşik demo yüklenemedi.',
        'Built-in demo could not be started.': 'Yerleşik demo başlatılamadı.',
        'No report is available yet.': 'Henüz indirilebilecek bir rapor yok.',
        'The latest report file was not found.': 'Son rapor dosyası diskte bulunamadı.',
        'Unable to load operators.': 'Operatör listesi yüklenemedi.',
        'Unable to refresh status.': 'Durum yenilenemedi.',
        'No Python source files matched the configured source paths and exclude patterns.': 'Ayarlanan source paths ve exclude kuralları ile eşleşen Python dosyası bulunamadı.',
        'Baseline test run failed. Fix the normal test suite first, then rerun mutation analysis.': 'Baseline test paketi başarısız oldu. Önce normal testlerini düzelt, sonra mutation analizini tekrar çalıştır.',
        'No mutants were executed. Check the source paths, exclude rules, and enabled operators.': 'Hiç mutant koşulmadı. Kaynak yollarını, exclude kurallarını ve seçili operatörleri kontrol et.',
        'All executed mutants were detected. Increase the scope or mutant count to probe more behavior.': 'Koşulan tüm mutantlar yakalandı. Daha fazla davranışı ölçmek için kapsamı ya da mutant sayısını artır.',
      };

      if (text in exactMatches) {
        return exactMatches[text];
      }

      let match = text.match(/^(\d+) mutant\(s\) survived\. Add focused assertions around the changed behavior\.$/);
      if (match) {
        return `${match[1]} mutant yaşadı. Değişen davranış etrafına hedefli assertion'lar ekle.`;
      }

      match = text.match(/^(\d+) mutant\(s\) timed out\. Review loops, waits, or raise the timeout budget\.$/);
      if (match) {
        return `${match[1]} mutant timeout oldu. Döngüleri, beklemeleri ve timeout bütçesini gözden geçir.`;
      }

      match = text.match(/^(\d+) mutant\(s\) produced import or syntax issues\. Inspect the generated change details\.$/);
      if (match) {
        return `${match[1]} mutant import ya da syntax problemi üretti. Üretilen değişim detaylarını incele.`;
      }

      match = text.match(/^None of the configured source paths exist\. Checked: (.+)$/);
      if (match) {
        return `Ayarlanan kaynak yollarının hiçbiri bulunamadı. Kontrol edilen: ${match[1]}`;
      }

      return text;
    }

    function applyStaticTranslations() {
      document.documentElement.lang = currentLanguage;
      langEnButton.classList.toggle('active', currentLanguage === 'en');
      langTrButton.classList.toggle('active', currentLanguage === 'tr');
      langEnButton.setAttribute('aria-pressed', currentLanguage === 'en' ? 'true' : 'false');
      langTrButton.setAttribute('aria-pressed', currentLanguage === 'tr' ? 'true' : 'false');
      langEnButton.setAttribute('title', languageValue('Switch to English', 'İngilizceye geç'));
      langTrButton.setAttribute('title', languageValue('Switch to Turkish', 'Türkçeye geç'));

      setText('.hero .eyebrow', 'Local Mutation Dashboard', 'Yerel Mutation Paneli');
      setText('.hero-copy', 'Run mutation analysis without leaving the browser. This page is both the control center and the onboarding guide: launch a session, watch the baseline, inspect survivors, and learn how to turn them into stronger tests.', "Tarayıcıdan çıkmadan mutation analizi çalıştır. Bu sayfa hem kontrol paneli hem de öğrenme rehberi olarak tasarlandı: koşuyu başlat, baseline'ı izle, survivor'ları incele ve bunları daha güçlü testlere nasıl dönüştüreceğini burada öğren.");
      setText('.pill-row .pill:nth-child(1)', 'Baseline test run comes first', 'Önce baseline test koşulur');
      setText('.pill-row .pill:nth-child(2)', 'Mutants are generated from the AST', 'AST ile mutant üretilir');
      setText('.pill-row .pill:nth-child(3)', 'Detailed usage guide included', 'Detaylı kullanım rehberi var');
      setText('.pill-row .pill:nth-child(4)', 'JSON report is preserved', 'JSON raporu saklanır');
      setLeadText('.hero > label', 'Choose a demo', 'Bir demo seç');
      setText('#starter-button', 'Use Starter Settings', 'Başlangıç Ayarlarını Doldur');
      setText('#demo-button', 'Load Selected Demo', 'Seçili Demoyu Yükle');
      setText('#demo-run-button', 'Run Selected Demo', 'Seçili Demoyu Çalıştır');
      setText('#guide-button', 'Open Usage Guide', 'Kullanım Rehberine Git');
      setHTML('#demo-inline-note', 'Load Selected Demo fills the form with the active demo settings. Run Selected Demo fills those values and starts the example immediately. After the run, use Download Latest Report or Download Latest PDF to save the results.', '<span class="inline-code">Seçili Demoyu Yükle</span> aktif demoya ait ayarları forma yerleştirir. <span class="inline-code">Seçili Demoyu Çalıştır</span> aynı değerleri doldurur ve örneği hemen başlatır. Koşudan sonra sonuçları kaydetmek için <span class="inline-code">Son JSON Raporunu İndir</span> veya <span class="inline-code">Son PDF Raporunu İndir</span> butonunu kullan.');

      setText('.tour-grid .tour-card:nth-child(1) h3', 'Start Small', 'Küçük Başla');
      setText('.tour-grid .tour-card:nth-child(1) p', 'Begin with one package or a batch of 10 mutants. Smaller runs make it easier to understand why a mutant survived.', 'Tek bir paket ya da 10 mutantlık bir batch ile başla. Küçük koşular bir mutantın neden yaşadığını anlamayı çok kolaylaştırır.');
      setText('.tour-grid .tour-card:nth-child(2) h3', 'Read the Changed Behavior', 'Değişen Davranışı Oku');
      setText('.tour-grid .tour-card:nth-child(2) p', 'A survivor means the tests still passed after behavior changed. The change itself is the clue for the next test you should write.', "Survivor demek, davranış değişmesine rağmen testlerin geçtiği anlamına gelir. Değişen ifade, yazman gereken bir sonraki test için en güçlü ipucudur.");
      setText('.tour-grid .tour-card:nth-child(3) h3', 'Improve and Rerun', 'Geliştir ve Tekrar Koş');
      setText('.tour-grid .tour-card:nth-child(3) p', 'Add one focused assertion for the missing behavior, rerun the same scope, then widen the run when the weak spot is closed.', 'Eksik davranış için tek bir net assertion ekle, aynı kapsamı tekrar koştur, boşluk kapanınca koşuyu genişlet.');

      setText('.grid > .panel:nth-child(1) h2', 'Run Setup', 'Çalıştırma Ayarları');
      setText('.grid > .panel:nth-child(1) .panel-copy', 'Choose a project, narrow the scope, and start the next mutation pass.', 'Projeyi seç, kapsamı daralt ve bir sonraki mutation koşusunu başlat.');
      setLeadText('#run-form > label:nth-of-type(1)', 'Project root', 'Proje kökü');
      setHTML('#run-form > label:nth-of-type(1) .field-help', 'The folder of the project you want to analyze. In most cases use <span class="inline-code">.</span> when the terminal is already inside that project.', 'Analiz etmek istediğin projenin klasörü. Terminal zaten projenin içindeyse genelde <span class="inline-code">.</span> kullanman yeterlidir.');
      setLeadText('#run-form > label:nth-of-type(2)', 'Config path', 'Config yolu');
      setPlaceholder('#config-path', 'Optional pyproject.toml path', 'Opsiyonel pyproject.toml yolu');
      setHTML('#run-form > label:nth-of-type(2) .field-help', 'Leave blank to use <span class="inline-code">pyproject.toml</span> from the project root.', 'Boş bırakırsan proje kökündeki <span class="inline-code">pyproject.toml</span> kullanılır.');
      setLeadText('#run-form > label:nth-of-type(3)', 'Source paths', 'Kaynak yollar');
      setHTML('#run-form > label:nth-of-type(3) .field-help', 'Comma-separated paths to mutate. Recommended first value: <span class="inline-code">src</span>.', 'Virgül ile ayrılmış mutate edilecek yollar. İlk deneme için önerilen değer: <span class="inline-code">src</span>.');
      setLeadText('#run-form > label:nth-of-type(4)', 'Operators', 'Operatörler');
      setText('#run-form > label:nth-of-type(4) .field-help', 'Leave all operators unselected to run the full default set. Select a subset only when you want a focused pass.', 'Hiçbirini seçmezsen varsayılan operatörlerin tamamı çalışır. Daha odaklı bir koşu istediğinde alt küme seç.');
      setLeadText('#run-form .split label:nth-child(1)', 'Max mutants', 'Maksimum mutant');
      setPlaceholder('#max-mutants', 'Optional', 'Opsiyonel');
      setText('#run-form .split label:nth-child(1) .field-help', 'Use 5-20 for an easy first run.', 'İlk deneme için 5-20 arası iyi bir aralıktır.');
      setLeadText('#run-form .split label:nth-child(2)', 'Timeout (sec)', 'Zaman aşımı (sn)');
      setPlaceholder('#timeout', 'Optional', 'Opsiyonel');
      setText('#run-form .split label:nth-child(2) .field-help', 'Leave blank to auto-calculate from the baseline run.', 'Boş bırakırsan baseline süresine göre otomatik hesaplanır.');
      setNestedLeadText('#stop-on-survivor + span', 'Stop after the first survivor', 'İlk survivor görülünce dur');
      setText('#stop-on-survivor + span .mini-note', 'Best for fast local feedback when you only need the first actionable gap.', 'Yerelde hızlı geri bildirim istediğinde ve ilk aksiyonluk boşluk yettiğinde idealdir.');
      setNestedLeadText('#fail-on-survivor + span', 'Fail run when a survivor appears', 'Survivor varsa koşuyu fail say');
      setText('#fail-on-survivor + span .mini-note', 'Best for CI or quality gates where any survivor should fail the run.', 'CI veya kalite kapısında tek bir survivor bile koşuyu başarısız saymalıysa kullan.');
      setText('#run-form .button-row button:nth-child(1)', 'Start Mutation Run', 'Mutation Koşusunu Başlat');
      setText('#form-demo-button', 'Load Selected Demo', 'Seçili Demoyu Forma Yerleştir');
      setText('#reset-button', 'Reset Form', 'Formu Temizle');
      setText('#refresh-button', 'Refresh Status', 'Durumu Yenile');

      setText('.grid > .panel:nth-child(2) h2', 'Control Room', 'Kontrol Odası');
      setText('.grid > .panel:nth-child(2) .panel-copy', 'Track the current state, the latest report path, and the headline mutation metrics here.', 'Güncel durumu, son rapor yolunu ve özet mutation metriklerini burada izle.');
      setText('.info-grid .info-card:nth-child(1) .info-key', 'Started', 'Başladı');
      setText('.info-grid .info-card:nth-child(2) .info-key', 'Finished', 'Bitti');
      setText('.info-grid .info-card:nth-child(3) .info-key', 'Report', 'Rapor');
      setText('.metric-grid .metric:nth-child(1) .metric-label', 'Score', 'Skor');
      setText('.metric-grid .metric:nth-child(2) .metric-label', 'Killed', 'Öldürülen');
      setText('.metric-grid .metric:nth-child(3) .metric-label', 'Survived', 'Yaşayan');
      setText('.metric-grid .metric:nth-child(4) .metric-label', 'Executed', 'Koşulan');
      setText('.metric-grid .metric:nth-child(5) .metric-label', 'Generated', 'Üretilen');
      setText('.metric-grid .metric:nth-child(6) .metric-label', 'Files', 'Dosya');
      setText('#download-report-button', 'Download Latest Report', 'Son JSON Raporunu İndir');
      setText('#download-pdf-button', 'Download Latest PDF', 'Son PDF Raporunu İndir');

      setText('#usage-guide h2', 'How To Use Mutation Lab', 'Mutation Lab Nasıl Kullanılır?');
      setText('#usage-guide > .panel-header .panel-copy', 'This guide is designed for both first-time users and teams turning mutation testing into a regular workflow.', "Bu rehber hem mutation testing'e ilk kez bakanlar hem de bunu düzenli bir kalite aracına dönüştürmek isteyen ekipler için hazırlandı.");
      setText('#usage-guide .step-card:nth-child(1) h3', 'Confirm the normal test suite is green', 'Normal test paketinin yeşil olduğunu doğrula');
      setText('#usage-guide .step-card:nth-child(1) p', 'Mutation testing only makes sense after the regular test suite passes. If the baseline fails, fix that first and try again.', 'Mutation testing ancak normal test paketi geçtikten sonra anlamlıdır. Baseline fail ise önce onu düzelt, sonra tekrar dene.');
      setText('#usage-guide .step-card:nth-child(2) h3', 'Choose a small scope', 'Küçük bir kapsam seç');
      setText('#usage-guide .step-card:nth-child(2) p', 'Start with <span class="inline-code">src</span> and around 10 mutants. That keeps the output readable and makes the first run much easier to learn from.', '<span class="inline-code">src</span> ve yaklaşık 10 mutant ile başla. Bu sayede çıktı daha okunabilir olur ve ilk koşudan bir şey öğrenmek çok daha kolaylaşır.');
      setHTML('#usage-guide .step-card:nth-child(2) p', 'Start with <span class="inline-code">src</span> and around 10 mutants. That keeps the output readable and makes the first run much easier to learn from.', '<span class="inline-code">src</span> ve yaklaşık 10 mutant ile başla. Bu sayede çıktı daha okunabilir olur ve ilk koşudan bir şey öğrenmek çok daha kolaylaşır.');
      setText('#usage-guide .step-card:nth-child(3) h3', 'Inspect survivors carefully', "Survivor'ları dikkatle incele");
      setText('#usage-guide .step-card:nth-child(3) p', 'A surviving mutant means tests still passed after the behavior changed. That usually means an edge case, branch, or assertion is missing.', "Survivor, davranış değişmesine rağmen testlerin geçtiğini söyler. Bu genelde eksik bir edge-case, branch ya da assertion olduğu anlamına gelir.");
      setText('#usage-guide .step-card:nth-child(4) h3', 'Add one focused test and rerun', 'Tek bir hedefli test ekle ve tekrar koş');
      setText('#usage-guide .step-card:nth-child(4) p', 'Read the original and mutated snippets, identify the changed expectation, write one targeted test, and rerun the same scope.', 'Orijinal ve mutate edilmiş parçayı oku, değişen beklentiyi bul, bir hedefli test yaz ve aynı kapsamı tekrar koştur.');
      setText('#usage-guide .details details:nth-child(1) summary', 'Recommended first run', 'Önerilen ilk koşu');
      setHTML('#usage-guide .details details:nth-child(1) p', 'If you are new to mutation testing, start with these values: project root <span class="inline-code">.</span>, source paths <span class="inline-code">src</span>, max mutants <span class="inline-code">10</span>, leave timeout blank, and keep both survivor checkboxes off.', "Mutation testing'e yeni başlıyorsan şu değerlerle başla: proje kökü <span class=\"inline-code\">.</span>, kaynak yollar <span class=\"inline-code\">src</span>, maksimum mutant <span class=\"inline-code\">10</span>, timeout boş, iki survivor kutucu da kapalı.");
      setText('#usage-guide .details details:nth-child(2) summary', 'How do I use the demo catalog?', 'Demo kataloğunu nasıl kullanırım?');
      setHTML('#usage-guide .details details:nth-child(2) p', 'Choose a demo first, then click <span class="inline-code">Load Selected Demo</span> to fill the form with that scenario. Review the values if you want to learn what each field means, then click <span class="inline-code">Start Mutation Run</span>. Use <span class="inline-code">Run Selected Demo</span> when you want one-click fill + run. After the run, keep the JSON report for tooling and download the PDF when you want a human-readable summary.', 'Önce bir demo seç, sonra o senaryonun ayarlarını forma yerleştirmek için <span class="inline-code">Seçili Demoyu Yükle</span> butonuna bas. Alanların ne anlama geldiğini öğrenmek istiyorsan önce değerleri incele, sonra <span class="inline-code">Mutation Koşusunu Başlat</span> seçeneğini kullan. Tek tık istersen <span class="inline-code">Seçili Demoyu Çalıştır</span> ile doldurup hemen koşabilirsin. Koşudan sonra araçlar için JSON raporunu sakla, insan okunur özet istediğinde PDF raporunu indir.');
      setText('#usage-guide .details details:nth-child(3) summary', 'What should you do after a survivor?', 'Survivor gördüğünde ne yapmalısın?');
      setHTML('#usage-guide .details details:nth-child(3) p', 'Example: if the tool shows <span class="inline-code">value &gt; 0 -&gt; value &gt;= 0</span> and that mutant survives, your tests probably never prove what should happen for <span class="inline-code">0</span>. Add a test for that exact boundary and rerun.', 'Örnek: araç <span class="inline-code">value &gt; 0 -&gt; value &gt;= 0</span> gösteriyorsa ve mutant yaşıyorsa, testlerin büyük ihtimalle <span class="inline-code">0</span> için doğru davranışı kanıtlamıyordur. Tam o sınır durumu için test ekle ve tekrar koş.');
      setText('#usage-guide .code-card .info-key', 'Starter pyproject.toml', 'Başlangıç pyproject.toml');

      setText('.guide-grid > .panel:nth-child(2) h2', 'Field Guide', 'Alan Rehberi');
      setText('.guide-grid > .panel:nth-child(2) .panel-copy', 'Use this as a quick reference for what belongs in each form field.', 'Formdaki her alan için ne yazman gerektiğini hızlı referans gibi kullan.');
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(1) summary', 'Project root', 'Proje kökü');
      setHTML('.guide-grid > .panel:nth-child(2) .details details:nth-child(1) p', 'The project folder you want to analyze. If the terminal is already in that folder, use <span class="inline-code">.</span>.', 'Analiz etmek istediğin projenin klasörü. Terminal zaten o klasördeyse <span class="inline-code">.</span> kullan.');
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(2) summary', 'Config path', 'Config yolu');
      setHTML('.guide-grid > .panel:nth-child(2) .details details:nth-child(2) p', 'Use this only if you want to point at a specific config file. In most cases leave it blank and let the tool load <span class="inline-code">pyproject.toml</span> automatically.', 'Config dosyasını elle göstermek istersen kullan. Çoğu durumda boş bırak ve aracın <span class="inline-code">pyproject.toml</span> dosyasını otomatik okumasına izin ver.');
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(3) summary', 'Source paths', 'Kaynak yollar');
      setHTML('.guide-grid > .panel:nth-child(2) .details details:nth-child(3) p', 'Comma-separated paths to mutate. Good examples are <span class="inline-code">src</span>, <span class="inline-code">src/my_package</span>, or <span class="inline-code">src/my_package/service.py</span>.', 'Virgül ile ayrılmış mutate edilecek yollar. İyi örnekler: <span class="inline-code">src</span>, <span class="inline-code">src/my_package</span> ya da <span class="inline-code">src/my_package/service.py</span>.');
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(4) summary', 'Operators', 'Operatörler');
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(4) p', 'Leave everything unselected to run all default operators. Choose a subset only when you want a specific kind of mutation pass.', 'Hiçbir şey seçmezsen varsayılan operatörlerin tamamı koşar. Sadece belli mutation tiplerine odaklanmak istediğinde alt küme seç.');
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(5) summary', 'Max mutants and timeout', 'Maksimum mutant ve timeout');
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(5) p', 'While learning, 5-20 mutants is a good range. Leave timeout blank unless your test suite genuinely needs a manual budget.', "Öğrenme aşamasında 5-20 mutant iyi bir aralıktır. Test paketin alışılmadık şekilde uzun sürmüyorsa timeout'u boş bırak.");
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(6) summary', 'Stop on survivor vs fail on survivor', "İlk survivor'da dur ve survivor varsa fail farkı");
      setText('.guide-grid > .panel:nth-child(2) .details details:nth-child(6) p', 'Stop on survivor is for fast local learning. Fail on survivor is for CI or stricter quality gates where even one survivor should fail the run.', "İlk survivor'da dur seçeneği yerelde hızlı öğrenme içindir. Survivor varsa fail seçeneği ise CI veya katı kalite kapıları içindir.");

      setText('.reference-grid > .panel:nth-child(1) h2', 'Result Legend', 'Sonuç Efsanesi');
      setText('.reference-grid > .panel:nth-child(1) .panel-copy', 'These are the outcomes you will see in the results table.', 'Sonuç tablosunda göreceğin durumlar bunlardır.');
      setText('.reference-grid > .panel:nth-child(1) .legend-card:nth-child(1) p', 'Tests failed after the mutation. This is good: the changed behavior was detected.', 'Mutation sonrası testler fail oldu. Bu iyidir; değişen davranış yakalandı.');
      setText('.reference-grid > .panel:nth-child(1) .legend-card:nth-child(2) p', 'Tests still passed after the mutation. This points to a missing assertion or edge case.', 'Mutation sonrası testler hâlâ geçti. Bu eksik assertion ya da edge-case işareti olabilir.');
      setText('.reference-grid > .panel:nth-child(1) .legend-card:nth-child(3) p', 'The mutated run took too long. Review loops, waits, or increase the timeout budget.', 'Mutate edilmiş koşu çok uzun sürdü. Döngüleri, beklemeleri ya da timeout bütçesini gözden geçir.');
      setText('.reference-grid > .panel:nth-child(1) .legend-card:nth-child(4) p', 'The mutation caused a syntax or import problem instead of a clean test failure.', 'Mutation temiz bir test faili yerine syntax ya da import problemi üretti.');

      setText('.reference-grid > .panel:nth-child(2) h2', 'CLI Equivalents', 'CLI Karşılıkları');
      setText('.reference-grid > .panel:nth-child(2) .panel-copy', 'The UI and CLI use the same engine. These commands match the common UI flows.', 'UI ve CLI aynı motoru kullanır. Bu komutlar en yaygın UI akışlarının terminal karşılığıdır.');
      setText('.reference-grid > .panel:nth-child(2) .code-card:nth-child(2) .info-key', 'Useful commands', 'Yararlı komutlar');
      setText('.reference-grid > .panel:nth-child(2) .code-card:nth-child(3) .info-key', 'Built-in demo', 'Yerleşik demo');
      setText('.reference-grid > .panel:nth-child(2) .code-card:nth-child(3) pre', 'Project root: examples/beginner_demo\nSource paths: src\nMax mutants: 10\nTimeout: leave blank', 'Proje kökü: examples/beginner_demo\nKaynak yollar: src\nMaksimum mutant: 10\nZaman aşımı: boş bırak');

      setText('.results h2', 'Results', 'Sonuçlar');
      setText('.results .panel-copy', 'Use surviving mutants to find weak assertions and missing edge-case tests.', "Yaşayan mutantları kullanarak zayıf assertion'ları ve eksik edge-case testlerini bul.");
      setText('.table-wrap thead th:nth-child(1)', 'Status', 'Durum');
      setText('.table-wrap thead th:nth-child(2)', 'File', 'Dosya');
      setText('.table-wrap thead th:nth-child(3)', 'Line', 'Satır');
      setText('.table-wrap thead th:nth-child(4)', 'Operator', 'Operatör');
      setText('.table-wrap thead th:nth-child(5)', 'Change', 'Değişim');
      setText('.table-wrap thead th:nth-child(6)', 'Summary', 'Özet');
    }

    function translateStatus(status) {
      const labels = currentLanguage === 'en'
        ? { idle: 'Idle', running: 'Running', completed: 'Completed', failed: 'Failed' }
        : { idle: 'Hazır', running: 'Çalışıyor', completed: 'Tamamlandı', failed: 'Hatalı' };
      return labels[status] || status;
    }

    function getInitialLanguage() {
      try {
        const stored = window.localStorage.getItem(languageStorageKey);
        return stored === 'tr' ? 'tr' : 'en';
      } catch {
        return 'en';
      }
    }

    function applyLanguage(language) {
      currentLanguage = language === 'tr' ? 'tr' : 'en';
      try {
        window.localStorage.setItem(languageStorageKey, currentLanguage);
      } catch {}
      applyStaticTranslations();
      populateDemoSelect();
      renderDemoDetails();
      renderStatus(lastSnapshot);
    }

    function selectedDemoId() {
      return demoSelect.value || 'beginner';
    }

    function findDemo(demoId) {
      return demoCatalog.find((demo) => demo.id === demoId) || demoCatalog[0] || null;
    }

    function populateDemoSelect() {
      const currentValue = selectedDemoId();
      demoSelect.innerHTML = '';
      demoCatalog.forEach((demo) => {
        const option = document.createElement('option');
        option.value = demo.id;
        option.textContent = languageValue(demo.name.en, demo.name.tr);
        option.selected = demo.id === currentValue;
        demoSelect.appendChild(option);
      });
      if (!findDemo(currentValue) && demoCatalog.length > 0) {
        demoSelect.value = demoCatalog[0].id;
      }
    }

    function renderDemoDetails() {
      const demo = findDemo(selectedDemoId());
      if (!demo) {
        demoSummary.textContent = '';
        demoGoal.textContent = '';
        return;
      }
      demoSummary.textContent = languageValue(demo.summary.en, demo.summary.tr);
      demoGoal.textContent = languageValue(
        `Learning goal: ${demo.learning_goal.en}`,
        `Öğrenme hedefi: ${demo.learning_goal.tr}`
      );
    }

    function parseCommaList(value) {
      return value
        .split(',')
        .map((item) => item.trim())
        .filter(Boolean);
    }

    function selectedOperators() {
      return Array.from(operatorSelect.selectedOptions).map((option) => option.value);
    }

    function clearOperatorSelection() {
      Array.from(operatorSelect.options).forEach((option) => {
        option.selected = false;
      });
    }

    function applyRequestToForm(request) {
      document.getElementById('project-root').value = request.project_root || '.';
      document.getElementById('config-path').value = request.config_path || '';
      document.getElementById('source-paths').value = (request.source_paths || []).join(', ');
      document.getElementById('max-mutants').value = request.max_mutants ?? '';
      document.getElementById('timeout').value = request.per_mutant_timeout ?? '';
      document.getElementById('stop-on-survivor').checked = Boolean(request.stop_on_survivor);
      document.getElementById('fail-on-survivor').checked = Boolean(request.fail_on_survivor);
      clearOperatorSelection();
      Array.from(operatorSelect.options).forEach((option) => {
        option.selected = (request.operators || []).includes(option.value);
      });
    }

    function applyStarterDefaults() {
      applyRequestToForm({
        project_root: '.',
        config_path: null,
        source_paths: ['src'],
        operators: [],
        max_mutants: 10,
        per_mutant_timeout: null,
        stop_on_survivor: false,
        fail_on_survivor: false,
      });
      statusMessage.textContent = languageValue(
        'Starter settings were loaded into the form.',
        'Başlangıç ayarları forma yerleştirildi.'
      );
    }

    async function loadDemoCatalog() {
      const response = await fetch('/api/demos');
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || 'Built-in demo could not be loaded.');
      }
      demoCatalog = payload.demos || demoCatalog;
      populateDemoSelect();
      renderDemoDetails();
    }

    async function fetchDemoPreset(demoId = selectedDemoId()) {
      const response = await fetch(`/api/demo-preset?demo_id=${encodeURIComponent(demoId)}`);
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || 'Built-in demo could not be loaded.');
      }
      return payload;
    }

    async function applyDemoPreset() {
      try {
        const demo = await fetchDemoPreset();
        applyRequestToForm(demo.request);
        renderDemoDetails();
        statusMessage.textContent = languageValue(
          `${findDemo(selectedDemoId())?.name.en || 'Selected demo'} loaded. Review the form, then click "Start Mutation Run" or use "Run Selected Demo" for one-click fill + run.`,
          `${findDemo(selectedDemoId())?.name.tr || 'Seçili demo'} yüklendi. Önce formu incele, sonra "Mutation Koşusunu Başlat" butonuna bas ya da tek tık için "Seçili Demoyu Çalıştır" seçeneğini kullan.`
        );
        document.getElementById('usage-guide').scrollIntoView({ behavior: 'smooth', block: 'start' });
      } catch (error) {
        const rawMessage = error instanceof Error ? error.message : 'Built-in demo could not be loaded.';
        const message = localizeBackendText(rawMessage);
        renderStatus({ status: 'failed', message, error: message });
      }
    }

    function resetFormToBlank() {
      document.getElementById('project-root').value = '.';
      document.getElementById('config-path').value = '';
      document.getElementById('source-paths').value = '';
      document.getElementById('max-mutants').value = '';
      document.getElementById('timeout').value = '';
      document.getElementById('stop-on-survivor').checked = false;
      document.getElementById('fail-on-survivor').checked = false;
      clearOperatorSelection();
      statusMessage.textContent = languageValue('Form cleared.', 'Form temizlendi.');
    }

    function buildFormPayload() {
      return {
        project_root: document.getElementById('project-root').value.trim() || '.',
        config_path: document.getElementById('config-path').value.trim() || null,
        source_paths: parseCommaList(document.getElementById('source-paths').value),
        operators: selectedOperators(),
        max_mutants: document.getElementById('max-mutants').value ? Number(document.getElementById('max-mutants').value) : null,
        per_mutant_timeout: document.getElementById('timeout').value ? Number(document.getElementById('timeout').value) : null,
        stop_on_survivor: document.getElementById('stop-on-survivor').checked,
        fail_on_survivor: document.getElementById('fail-on-survivor').checked,
      };
    }

    async function startMutationRun(payload) {
      const response = await fetch('/api/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      if (!response.ok) {
        const rawMessage = data.detail || 'Unable to start run.';
        renderStatus({
          status: 'failed',
          message: localizeBackendText(rawMessage),
          error: localizeBackendText(rawMessage),
        });
        return;
      }
      renderStatus(data);
    }

    async function runBuiltInDemo() {
      try {
        const demo = await fetchDemoPreset();
        applyRequestToForm(demo.request);
        renderDemoDetails();
        statusMessage.textContent = languageValue(
          `${findDemo(selectedDemoId())?.name.en || 'Selected demo'} is starting now. The chosen example is designed to teach a specific mutation-testing scenario.`,
          `${findDemo(selectedDemoId())?.name.tr || 'Seçili demo'} şimdi başlıyor. Seçtiğin örnek, belirli bir mutation-testing senaryosunu öğretmek için tasarlandı.`
        );
        await startMutationRun(demo.request);
      } catch (error) {
        const rawMessage = error instanceof Error ? error.message : 'Built-in demo could not be started.';
        const message = localizeBackendText(rawMessage);
        renderStatus({ status: 'failed', message, error: message });
      }
    }

    function downloadLatestReport() {
      if (!lastSnapshot.report_path) {
        statusMessage.textContent = languageValue(
          'There is no report to download yet.',
          'İndirilecek bir rapor henüz yok.'
        );
        return;
      }
      window.location.href = '/api/report/download';
    }

    function downloadLatestPdf() {
      if (!lastSnapshot.pdf_report_path) {
        statusMessage.textContent = languageValue(
          'There is no PDF report to download yet.',
          'İndirilecek bir PDF raporu henüz yok.'
        );
        return;
      }
      window.location.href = '/api/report/download/pdf';
    }

    async function loadOperators() {
      const response = await fetch('/api/operators');
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || 'Unable to load operators.');
      }
      operatorSelect.innerHTML = '';
      payload.operators.forEach((name) => {
        const option = document.createElement('option');
        option.value = name;
        option.textContent = name;
        operatorSelect.appendChild(option);
      });
    }

    function renderRequest(request) {
      if (!request) {
        requestHint.innerHTML = '';
        return;
      }

      const sources = (request.source_paths || []).join(', ') || languageValue('config default', 'config varsayılanı');
      const operators = (request.operators || []).join(', ') || languageValue('all operators', 'tüm operatörler');
      const stopOnSurvivor = request.stop_on_survivor ? languageValue('enabled', 'açık') : languageValue('disabled', 'kapalı');
      const failOnSurvivor = request.fail_on_survivor ? languageValue('enabled', 'açık') : languageValue('disabled', 'kapalı');
      requestHint.innerHTML = `
        <div class="info-card">
          <span class="info-key">${escapeHtml(languageValue('Last request', 'Son istek'))}</span>
          <div><strong>${escapeHtml(languageValue('Project', 'Proje'))}:</strong> ${escapeHtml(request.project_root)}</div>
          <div><strong>${escapeHtml(languageValue('Sources', 'Kaynaklar'))}:</strong> ${escapeHtml(sources)}</div>
          <div><strong>${escapeHtml(languageValue('Operators', 'Operatörler'))}:</strong> ${escapeHtml(operators)}</div>
        </div>
        <div class="info-card">
          <span class="info-key">${escapeHtml(languageValue('Run policy', 'Koşu politikası'))}</span>
          <div><strong>${escapeHtml(languageValue('Stop on survivor', "İlk survivor'da dur"))}:</strong> ${escapeHtml(stopOnSurvivor)}</div>
          <div><strong>${escapeHtml(languageValue('Fail on survivor', 'Survivor varsa fail'))}:</strong> ${escapeHtml(failOnSurvivor)}</div>
          <div><strong>${escapeHtml(languageValue('Max mutants', 'Maksimum mutant'))}:</strong> ${escapeHtml(request.max_mutants ?? languageValue('not set', 'ayarlanmadı'))}</div>
        </div>
      `;
    }

    function renderBaseline(baseline) {
      if (!baseline) {
        baselinePanel.innerHTML = `<strong>Baseline</strong><p class="panel-copy">${escapeHtml(languageValue('No run yet.', 'Henüz bir koşu yok.'))}</p>`;
        return;
      }

      const state = baseline.success ? languageValue('passed', 'geçti') : languageValue('failed', 'başarısız');
      baselinePanel.innerHTML = `
        <strong>Baseline ${escapeHtml(state)}</strong>
        <p class="panel-copy">${escapeHtml(languageValue('Command', 'Komut'))}: ${escapeHtml((baseline.command || []).join(' '))}</p>
        <p class="panel-copy">${escapeHtml(languageValue('Duration', 'Süre'))}: ${escapeHtml((baseline.duration_seconds || 0).toFixed(2))}${escapeHtml(languageValue('s', 'sn'))}</p>
        <div class="details">
          <details>
            <summary>${escapeHtml(languageValue('Baseline output', 'Baseline çıktı'))}</summary>
            <pre>${escapeHtml([baseline.stdout || '', baseline.stderr || ''].join('\n').trim() || languageValue('No output', 'Çıktı yok'))}</pre>
          </details>
        </div>
      `;
    }

    function renderMutants(mutants) {
      if (!mutants || mutants.length === 0) {
        mutantBody.innerHTML = `<tr><td colspan="6" class="empty">${escapeHtml(languageValue('No executed mutants yet.', 'Henüz koşulmuş mutant yok.'))}</td></tr>`;
        return;
      }

      mutantBody.innerHTML = mutants.map((mutant) => {
        const status = escapeHtml(mutant.status || 'unknown');
        const location = mutant.location || {};
        const summary = mutant.failing_summary || mutant.description || '-';
        return `
          <tr>
            <td><span class="chip chip-${status}">${status}</span></td>
            <td>${escapeHtml(mutant.file_path)}</td>
            <td>${escapeHtml(location.start_line ?? '-')}</td>
            <td>${escapeHtml(mutant.operator_name)}</td>
            <td><code>${escapeHtml(mutant.original_snippet)} -> ${escapeHtml(mutant.mutated_snippet)}</code></td>
            <td>${escapeHtml(summary)}</td>
          </tr>
        `;
      }).join('');
    }

    function renderSummary(summary) {
      if (!summary) {
        scoreValue.textContent = '0%';
        killedValue.textContent = '0';
        survivedValue.textContent = '0';
        executedValue.textContent = '0';
        generatedValue.textContent = '0';
        discoveredValue.textContent = '0';
        summaryCallout.innerHTML = `
          <strong>${escapeHtml(languageValue('Ready for your first run.', 'İlk koşuna hazırsın.'))}</strong>
          <p class="panel-copy">${escapeHtml(languageValue('Start with a small batch, inspect the surviving change, and turn it into a focused test.', 'Küçük bir batch ile başla, yaşayan değişikliği incele ve onu hedefli bir teste dönüştür.'))}</p>
        `;
        return;
      }

      scoreValue.textContent = `${Number(summary.mutation_score || 0).toFixed(1)}%`;
      killedValue.textContent = String(summary.killed || 0);
      survivedValue.textContent = String(summary.survived || 0);
      executedValue.textContent = String(summary.executed || 0);
      generatedValue.textContent = String(summary.generated_mutants || 0);
      discoveredValue.textContent = String((summary.discovered_files || []).length);

      if (summary.survived > 0) {
        summaryCallout.innerHTML = `
          <strong>${escapeHtml(summary.survived)} ${escapeHtml(languageValue('survivor(s) need attention.', 'survivor dikkat bekliyor.'))}</strong>
          <p class="panel-copy">${escapeHtml(languageValue('Read the changed behavior below, then add the smallest test that proves the intended result.', 'Aşağıdaki değişen davranışı oku, sonra beklenen sonucu kanıtlayan en küçük testi ekle.'))}</p>
        `;
      } else if (summary.executed > 0) {
        summaryCallout.innerHTML = `
          <strong>${escapeHtml(languageValue('No survivors in the latest executed set.', 'Son koşuda survivor yok.'))}</strong>
          <p class="panel-copy">${escapeHtml(languageValue('That means the current mutant batch was fully detected by your tests.', "Bu, mevcut mutant batch'inin testler tarafından tamamen yakalandığı anlamına gelir."))}</p>
        `;
      } else {
        summaryCallout.innerHTML = `
          <strong>${escapeHtml(languageValue('No mutants executed yet.', 'Henüz mutant koşulmadı.'))}</strong>
          <p class="panel-copy">${escapeHtml(languageValue('Check the source paths, exclude rules, and operator selection.', 'Kaynak yollarını, exclude kurallarını ve operatör seçimini kontrol et.'))}</p>
        `;
      }
    }

    function renderStatus(snapshot) {
      lastSnapshot = snapshot;
      const status = snapshot.status || 'idle';
      statusBadge.className = `status-badge status-${status}`;
      statusBadge.textContent = translateStatus(status);
      statusMessage.textContent = localizeBackendText(snapshot.error || snapshot.message || languageValue('No status yet.', 'Durum bilgisi yok.'));
      startedAt.textContent = formatTime(snapshot.started_at);
      finishedAt.textContent = formatTime(snapshot.finished_at);
      reportPath.textContent = snapshot.report_path || '-';
      renderRequest(snapshot.request);

      if (!snapshot.result) {
        renderBaseline(null);
        renderSummary(null);
        renderGuidance([]);
        renderMutants([]);
        return;
      }

      renderBaseline(snapshot.result.baseline);
      renderSummary(snapshot.result.summary);
      renderGuidance(snapshot.result.guidance || []);
      renderMutants(snapshot.result.mutants || []);
    }

    function renderGuidance(guidance) {
      if (!guidance || guidance.length === 0) {
        guidancePanel.innerHTML = `
          <strong>${escapeHtml(languageValue('Next-step guidance will appear here.', 'Bir sonraki adım önerileri burada görünecek.'))}</strong>
          <p class="panel-copy">${escapeHtml(languageValue('After a run, this panel summarizes what to do next.', 'Koşu tamamlandıktan sonra burada ne yapman gerektiği özetlenir.'))}</p>
        `;
        return;
      }

      const items = guidance.map((item) => `<li>${escapeHtml(localizeBackendText(item))}</li>`).join('');
      guidancePanel.innerHTML = `
        <strong>${escapeHtml(languageValue('Recommended next steps', 'Önerilen sonraki adımlar'))}</strong>
        <ul>${items}</ul>
      `;
    }

    async function refreshStatus() {
      const response = await fetch('/api/status');
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || 'Unable to refresh status.');
      }
      renderStatus(payload);
    }

    async function initializePage() {
      applyLanguage(getInitialLanguage());
      try {
        await loadDemoCatalog();
        await loadOperators();
        await refreshStatus();
      } catch (error) {
        const rawMessage = error instanceof Error ? error.message : 'Unable to refresh status.';
        const message = localizeBackendText(rawMessage);
        renderStatus({ status: 'failed', message, error: message });
      }
    }

    async function submitRun(event) {
      event.preventDefault();
      await startMutationRun(buildFormPayload());
    }

    form.addEventListener('submit', submitRun);
    refreshButton.addEventListener('click', refreshStatus);
    demoButton.addEventListener('click', applyDemoPreset);
    demoRunButton.addEventListener('click', runBuiltInDemo);
    formDemoButton.addEventListener('click', applyDemoPreset);
    demoSelect.addEventListener('change', renderDemoDetails);
    starterButton.addEventListener('click', applyStarterDefaults);
    resetButton.addEventListener('click', resetFormToBlank);
    langEnButton.addEventListener('click', () => applyLanguage('en'));
    langTrButton.addEventListener('click', () => applyLanguage('tr'));
    guideButton.addEventListener('click', () => {
      document.getElementById('usage-guide').scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    downloadReportButton.addEventListener('click', downloadLatestReport);
    downloadPdfButton.addEventListener('click', downloadLatestPdf);
    initializePage();
    setInterval(() => {
      refreshStatus().catch(() => {});
    }, 2000);
  </script>
</body>
</html>
"""
