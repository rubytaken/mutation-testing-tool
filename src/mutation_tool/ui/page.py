# ruff: noqa: E501

INDEX_HTML = """
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
      --danger: #aa3f2a;
      --success: #1b7f5d;
      --muted: #53656d;
      --shadow: 0 24px 60px rgba(18, 34, 43, 0.12);
      --radius: 22px;
    }

    * { box-sizing: border-box; }

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
      width: min(1180px, calc(100% - 32px));
      margin: 28px auto 48px;
      position: relative;
      z-index: 1;
    }

    .hero,
    .panel {
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
      gap: 14px;
      animation: rise 0.45s ease-out;
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
      max-width: 64ch;
      color: var(--muted);
      font-size: 1rem;
      line-height: 1.6;
    }

    .pill-row {
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

    .grid {
      display: grid;
      grid-template-columns: minmax(320px, 400px) minmax(0, 1fr);
      gap: 18px;
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

    .stack {
      display: grid;
      gap: 14px;
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

    .split {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }

    .checkbox {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
    }

    .checkbox input {
      width: 18px;
      height: 18px;
      padding: 0;
    }

    .button-row {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 6px;
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
      grid-template-columns: repeat(4, minmax(0, 1fr));
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

    .baseline,
    .survivor-callout {
      border-radius: 18px;
      padding: 16px;
      background: rgba(255, 255, 255, 0.72);
      border: 1px solid rgba(18, 34, 43, 0.08);
      margin-top: 14px;
    }

    .survivor-callout {
      border-left: 5px solid var(--accent);
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

    @keyframes rise {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 980px) {
      .grid,
      .metric-grid,
      .info-grid,
      .split {
        grid-template-columns: 1fr;
      }

      .shell {
        width: min(100% - 20px, 1180px);
      }
    }
  </style>
</head>
<body>
  <div class="shell">
    <section class="hero">
      <div class="eyebrow">Local Mutation Dashboard</div>
      <h1>Mutation Lab</h1>
      <p class="hero-copy">
        Run mutation analysis without leaving the browser. Launch a session, watch the baseline,
        and inspect the mutants that survived your tests.
      </p>
      <div class="pill-row">
        <div class="pill">Baseline test run first</div>
        <div class="pill">AST-generated mutants</div>
        <div class="pill">JSON report preserved</div>
      </div>
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
          </label>

          <label>
            Config path
            <input id="config-path" name="config_path" placeholder="Optional pyproject.toml path">
          </label>

          <label>
            Source paths
            <input id="source-paths" name="source_paths" placeholder="src, package/module.py">
          </label>

          <label>
            Operators
            <select id="operators" name="operators" multiple></select>
          </label>

          <div class="split">
            <label>
              Max mutants
              <input id="max-mutants" name="max_mutants" type="number" min="1" placeholder="Optional">
            </label>

            <label>
              Timeout (sec)
              <input id="timeout" name="per_mutant_timeout" type="number" min="0.1" step="0.1" placeholder="Optional">
            </label>
          </div>

          <label class="checkbox">
            <input id="fail-on-survivor" type="checkbox">
            Fail run when a survivor appears
          </label>

          <div class="button-row">
            <button class="primary" type="submit">Start Mutation Run</button>
            <button class="ghost" type="button" id="refresh-button">Refresh Status</button>
          </div>
        </form>
      </section>

      <section class="panel">
        <div class="panel-header">
          <div>
            <h2>Control Room</h2>
            <p class="panel-copy">Track current activity, recent report path, and headline mutation metrics.</p>
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
        </div>

        <div id="request-hint" class="details"></div>
      </section>
    </div>

    <section class="panel results">
      <div class="panel-header">
        <div>
          <h2>Results</h2>
          <p class="panel-copy">Use surviving mutants to find weak assertions and missing edge-case tests.</p>
        </div>
      </div>

      <div id="baseline-panel" class="baseline">
        <strong>Baseline</strong>
        <p class="panel-copy">No run yet.</p>
      </div>

      <div id="survivor-callout"></div>

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
              <td colspan="6" class="empty">Run a session to inspect individual mutants.</td>
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
    const mutantBody = document.getElementById('mutant-body');
    const baselinePanel = document.getElementById('baseline-panel');
    const survivorCallout = document.getElementById('survivor-callout');
    const requestHint = document.getElementById('request-hint');
    const operatorSelect = document.getElementById('operators');
    const form = document.getElementById('run-form');
    const refreshButton = document.getElementById('refresh-button');

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

    function parseCommaList(value) {
      return value
        .split(',')
        .map((item) => item.trim())
        .filter(Boolean);
    }

    function selectedOperators() {
      return Array.from(operatorSelect.selectedOptions).map((option) => option.value);
    }

    async function loadOperators() {
      const response = await fetch('/api/operators');
      const payload = await response.json();
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

      const sources = (request.source_paths || []).join(', ') || 'config default';
      const operators = (request.operators || []).join(', ') || 'all operators';
      requestHint.innerHTML = `
        <div class="info-card">
          <span class="info-key">Last request</span>
          <div><strong>Project:</strong> ${escapeHtml(request.project_root)}</div>
          <div><strong>Sources:</strong> ${escapeHtml(sources)}</div>
          <div><strong>Operators:</strong> ${escapeHtml(operators)}</div>
        </div>
      `;
    }

    function renderBaseline(baseline) {
      if (!baseline) {
        baselinePanel.innerHTML = '<strong>Baseline</strong><p class="panel-copy">No run yet.</p>';
        return;
      }

      const state = baseline.success ? 'passed' : 'failed';
      baselinePanel.innerHTML = `
        <strong>Baseline ${escapeHtml(state)}</strong>
        <p class="panel-copy">Command: ${escapeHtml((baseline.command || []).join(' '))}</p>
        <p class="panel-copy">Duration: ${escapeHtml((baseline.duration_seconds || 0).toFixed(2))}s</p>
        <div class="details">
          <details>
            <summary>Baseline output</summary>
            <pre>${escapeHtml([baseline.stdout || '', baseline.stderr || ''].join('\n').trim() || 'No output')}</pre>
          </details>
        </div>
      `;
    }

    function renderMutants(mutants) {
      if (!mutants || mutants.length === 0) {
        mutantBody.innerHTML = '<tr><td colspan="6" class="empty">No executed mutants yet.</td></tr>';
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
        survivorCallout.innerHTML = '';
        return;
      }

      scoreValue.textContent = `${Number(summary.mutation_score || 0).toFixed(1)}%`;
      killedValue.textContent = String(summary.killed || 0);
      survivedValue.textContent = String(summary.survived || 0);
      executedValue.textContent = String(summary.executed || 0);

      if (summary.survived > 0) {
        survivorCallout.className = 'survivor-callout';
        survivorCallout.innerHTML = `
          <strong>${escapeHtml(summary.survived)} survivor(s) need attention.</strong>
          <p class="panel-copy">Start by inspecting the surviving mutants below and add tests that prove the intended behavior.</p>
        `;
      } else {
        survivorCallout.className = 'survivor-callout';
        survivorCallout.innerHTML = `
          <strong>No survivors in the latest executed set.</strong>
          <p class="panel-copy">That means the current mutant batch was fully detected by your tests.</p>
        `;
      }
    }

    function renderStatus(snapshot) {
      const status = snapshot.status || 'idle';
      statusBadge.className = `status-badge status-${status}`;
      statusBadge.textContent = status.charAt(0).toUpperCase() + status.slice(1);
      statusMessage.textContent = snapshot.error || snapshot.message || 'No status yet.';
      startedAt.textContent = formatTime(snapshot.started_at);
      finishedAt.textContent = formatTime(snapshot.finished_at);
      reportPath.textContent = snapshot.report_path || '-';
      renderRequest(snapshot.request);

      if (!snapshot.result) {
        renderBaseline(null);
        renderSummary(null);
        renderMutants([]);
        return;
      }

      renderBaseline(snapshot.result.baseline);
      renderSummary(snapshot.result.summary);
      renderMutants(snapshot.result.mutants || []);
    }

    async function refreshStatus() {
      const response = await fetch('/api/status');
      const payload = await response.json();
      renderStatus(payload);
    }

    async function submitRun(event) {
      event.preventDefault();
      const payload = {
        project_root: document.getElementById('project-root').value.trim() || '.',
        config_path: document.getElementById('config-path').value.trim() || null,
        source_paths: parseCommaList(document.getElementById('source-paths').value),
        operators: selectedOperators(),
        max_mutants: document.getElementById('max-mutants').value ? Number(document.getElementById('max-mutants').value) : null,
        per_mutant_timeout: document.getElementById('timeout').value ? Number(document.getElementById('timeout').value) : null,
        fail_on_survivor: document.getElementById('fail-on-survivor').checked,
      };

      const response = await fetch('/api/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      if (!response.ok) {
        renderStatus({ status: 'failed', message: data.detail || 'Unable to start run.', error: data.detail || 'Unable to start run.' });
        return;
      }
      renderStatus(data);
    }

    form.addEventListener('submit', submitRun);
    refreshButton.addEventListener('click', refreshStatus);
    loadOperators().then(refreshStatus);
    setInterval(refreshStatus, 2000);
  </script>
</body>
</html>
"""
