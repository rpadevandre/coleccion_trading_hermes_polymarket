const config = window.ADMIN_CONFIG;
    const $ = (id) => document.getElementById(id);

    function baseUrl() {
      return $("apiBase").value.replace(/\/$/, "");
    }

    function writeOutput(data) {
      $("output").textContent = typeof data === "string" ? data : JSON.stringify(data, null, 2);
    }

    async function request(path, options = {}) {
      const response = await fetch(`${baseUrl()}${path}`, {
        headers: { "Content-Type": "application/json", ...(options.headers || {}) },
        ...options,
      });
      const text = await response.text();
      let data;
      try { data = text ? JSON.parse(text) : {}; } catch { data = text; }
      if (!response.ok) throw new Error(JSON.stringify(data, null, 2));
      return data;
    }

    function buildIntakePayload() {
      const raw = JSON.parse($("samplePayload").value);
      return {
        source: "admin_panel_demo",
        contact_name: "Sample Operator Lead",
        contact_email: "sample@example.com",
        company_or_location: config.title,
        message: raw.message,
        signals: raw.signals || {},
        consent_for_followup: false,
      };
    }

    $("loadSample").addEventListener("click", () => {
      $("samplePayload").value = "{\n  \"message\": \"Emergency AC repair request after-hours. Customer left voicemail and needs callback today.\",\n  \"signals\": {\n    \"service_type\": \"AC repair\",\n    \"after_hours\": true,\n    \"zip_code\": \"33101\",\n    \"call_time\": \"18:42\"\n  }\n}";
      writeOutput("Sample payload loaded.");
    });

    $("checkHealth").addEventListener("click", async () => {
      try {
        const [health, meta] = await Promise.all([request("/health"), request("/meta")]);
        $("apiStatus").textContent = health.status === "ok" ? "Healthy" : "Unexpected";
        $("primaryMetric").textContent = meta.expected_signals.length + " tracked signals";
        $("secondaryMetric").textContent = meta.ai_modules.length + " modules";
        writeOutput({ health, meta });
      } catch (error) {
        $("apiStatus").textContent = "Offline";
        writeOutput(`API check failed. Start FastAPI backend first.

${error.message}`);
      }
    });

    $("createIntake").addEventListener("click", async () => {
      try {
        const data = await request("/intakes", { method: "POST", body: JSON.stringify(buildIntakePayload()) });
        writeOutput(data);
      } catch (error) { writeOutput(error.message); }
    });

    $("scoreAssessment").addEventListener("click", async () => {
      try {
        const payload = JSON.parse($("samplePayload").value);
        const data = await request("/assessments/score", { method: "POST", body: JSON.stringify(payload) });
        writeOutput(data);
      } catch (error) { writeOutput(error.message); }
    });

    $("loadQueue").addEventListener("click", async () => {
      try {
        const data = await request("/admin/queue");
        const list = $("queueList");
        list.innerHTML = "";
        if (!data.length) {
          list.innerHTML = "<li>No queue items yet. Create a sample intake first.</li>";
        } else {
          data.forEach((item) => {
            const li = document.createElement("li");
            li.innerHTML = `<strong>${item.priority}</strong><br>${item.message_preview}<br><small>${item.next_action}</small>`;
            list.appendChild(li);
          });
        }
        writeOutput(data);
      } catch (error) { writeOutput(error.message); }
    });

    document.querySelectorAll(".view-tab").forEach((button) => {
      button.addEventListener("click", () => writeOutput(`Selected admin view: ${button.dataset.view}`));
    });
