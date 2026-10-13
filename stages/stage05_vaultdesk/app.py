from flask import Flask, request, redirect, session, render_template_string, abort

app = Flask(__name__)
app.secret_key = "shadowvault-dev-secret"

BASE = "/vaultdesk"

USERS = {
    "analyst": {
        "password": "vaultdesk2026",
        "role": "analyst"
    }
}

INCIDENTS = {
    101: {
        "owner": "analyst",
        "title": "Routine Endpoint Alert",
        "body": "Minor endpoint alert. No ShadowVault impact identified."
    },
    102: {
        "owner": "analyst",
        "title": "Archive Access Review",
        "body": "Analyst review completed. No privileged evidence attached."
    },
    900: {
        "owner": "security-admin",
        "title": "Restricted ShadowVault Incident",
        "body": """
Restricted Investigation Record

FLAG: SHADOW{vaultdesk_access_control_broken}

STAGE6_HOST: localhost
STAGE6_PORT: 2222
STAGE6_USER: investigator
STAGE6_PASS: nightwatch2026
"""
    }
}

STYLE = """
<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

:root{
    --bg:#0b0c09;
    --panel:#11130f;
    --panel2:#151811;
    --lime:#caff18;
    --lime-soft:#e2ff7c;
    --text:#f4f5ef;
    --muted:#858b7f;
    --line:rgba(255,255,255,.07);
    --lime-line:rgba(202,255,24,.18);
    --danger:#ff6b6b;
}

body{
    min-height:100vh;
    color:var(--text);
    background:
        radial-gradient(circle at 80% 15%, rgba(202,255,24,.045), transparent 25%),
        #0b0c09;
    font-family:Arial,Helvetica,sans-serif;
    overflow-x:hidden;
}

body::before{
    content:"";
    position:fixed;
    inset:0;
    z-index:-2;
    pointer-events:none;
    background-image:
        linear-gradient(rgba(202,255,24,.025) 1px,transparent 1px),
        linear-gradient(90deg,rgba(202,255,24,.025) 1px,transparent 1px);
    background-size:48px 48px;
    opacity:.2;
}

body::after{
    content:"";
    position:fixed;
    top:-200px;
    left:0;
    right:0;
    height:170px;
    z-index:-1;
    pointer-events:none;
    background:linear-gradient(
        transparent,
        rgba(202,255,24,.03),
        transparent
    );
    animation:scan 8s linear infinite;
}

@keyframes scan{
    to{
        transform:translateY(120vh);
    }
}

@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

@keyframes pulse{
    50%{
        opacity:.35;
        transform:scale(.75);
    }
}

header{
    height:76px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 6%;
    border-bottom:1px solid var(--line);
    background:rgba(9,10,8,.93);
    backdrop-filter:blur(14px);
}

.brand{
    display:flex;
    align-items:center;
    gap:13px;
}

.brand-mark{
    width:38px;
    height:38px;
    display:grid;
    place-items:center;
    border:1px solid var(--lime);
    color:var(--lime);
    font-weight:900;
}

.brand strong{
    display:block;
    font-size:15px;
}

.brand small{
    display:block;
    margin-top:3px;
    color:#6d7367;
    font-size:9px;
    letter-spacing:1.8px;
    text-transform:uppercase;
}

.status{
    display:flex;
    align-items:center;
    gap:8px;
    color:#777d70;
    font-family:Consolas,monospace;
    font-size:10px;
}

.dot{
    width:6px;
    height:6px;
    border-radius:50%;
    background:var(--lime);
    box-shadow:0 0 10px var(--lime);
    animation:pulse 1.7s infinite;
}

.wrapper{
    max-width:1180px;
    margin:auto;
    padding:70px 6% 100px;
    animation:fadeUp .7s ease both;
}

.label{
    color:var(--lime);
    font-size:10px;
    font-weight:900;
    letter-spacing:2px;
    text-transform:uppercase;
    margin-bottom:15px;
}

h1{
    font-size:clamp(42px,6vw,72px);
    line-height:.95;
    letter-spacing:-3px;
}

.subtitle{
    margin-top:18px;
    color:#8d9284;
    line-height:1.7;
    max-width:650px;
    font-size:14px;
}

.panel{
    margin-top:35px;
    border:1px solid var(--line);
    background:rgba(16,18,14,.82);
    position:relative;
}

.panel::before{
    content:"";
    position:absolute;
    left:-1px;
    top:-1px;
    width:65px;
    height:2px;
    background:var(--lime);
}

.panel-inner{
    padding:30px;
}

.login-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:60px;
    align-items:center;
}

.system-info{
    font-family:Consolas,monospace;
    font-size:11px;
    color:#777d70;
    line-height:2;
}

.system-info span{
    color:var(--lime);
}

label{
    display:block;
    margin-bottom:8px;
    color:#8f9588;
    font-size:10px;
    font-weight:900;
    letter-spacing:1.5px;
    text-transform:uppercase;
}

input{
    width:100%;
    padding:13px 14px;
    margin-bottom:20px;
    background:#0d0f0b;
    color:white;
    border:1px solid var(--line);
    outline:none;
    font-family:Consolas,monospace;
}

input:focus{
    border-color:var(--lime);
    box-shadow:0 0 0 2px rgba(202,255,24,.05);
}

button,
.btn{
    display:inline-block;
    padding:13px 18px;
    border:1px solid var(--lime);
    background:var(--lime);
    color:#10120c;
    font-weight:900;
    font-size:11px;
    letter-spacing:.7px;
    text-transform:uppercase;
    text-decoration:none;
    cursor:pointer;
    transition:.25s ease;
}

button:hover,
.btn:hover{
    transform:translateY(-2px);
    box-shadow:0 0 24px rgba(202,255,24,.16);
}

.btn-outline{
    background:transparent;
    color:var(--lime);
    border-color:var(--lime-line);
}

.error{
    margin-top:18px;
    padding:12px 14px;
    border:1px solid rgba(255,107,107,.25);
    color:#ff9999;
    background:rgba(255,107,107,.05);
    font-size:12px;
}

.dashboard-top{
    display:flex;
    align-items:flex-end;
    justify-content:space-between;
    gap:20px;
    margin-bottom:25px;
}

.userbox{
    color:#777d70;
    font-family:Consolas,monospace;
    font-size:10px;
    text-align:right;
}

.userbox strong{
    display:block;
    color:var(--lime);
    margin-top:4px;
    font-size:12px;
}

.incidents{
    border-top:1px solid var(--line);
}

.incident-row{
    display:grid;
    grid-template-columns:90px 1fr 150px;
    gap:20px;
    align-items:center;
    min-height:120px;
    padding:24px 18px;
    border-bottom:1px solid var(--line);
    text-decoration:none;
    color:white;
    position:relative;
    overflow:hidden;
    transition:.3s ease;
}

.incident-row::before{
    content:"";
    position:absolute;
    inset:0;
    background:linear-gradient(
        90deg,
        rgba(202,255,24,.05),
        transparent 40%
    );
    opacity:0;
    transition:.3s ease;
}

.incident-row:hover{
    padding-left:26px;
    background:#11130f;
    border-color:var(--lime-line);
}

.incident-row:hover::before{
    opacity:1;
}

.incident-row > *{
    position:relative;
    z-index:1;
}

.incident-id{
    font-family:Consolas,monospace;
    color:var(--lime);
    font-size:12px;
}

.incident-title{
    font-size:20px;
    margin-bottom:7px;
}

.incident-meta{
    color:#72786c;
    font-size:11px;
}

.open-label{
    justify-self:end;
    color:#7c8275;
    font-family:Consolas,monospace;
    font-size:9px;
    letter-spacing:1px;
}

.incident-box{
    margin-top:30px;
    border:1px solid var(--line);
    background:#0e100c;
}

.incident-head{
    padding:20px 24px;
    border-bottom:1px solid var(--line);
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.incident-head span{
    font-family:Consolas,monospace;
    font-size:10px;
    color:var(--lime);
}

pre{
    margin:0;
    padding:28px;
    white-space:pre-wrap;
    word-break:break-word;
    color:#d9ded1;
    font-family:Consolas,monospace;
    font-size:13px;
    line-height:1.9;
    background:#0b0d09;
}

.actions{
    margin-top:24px;
    display:flex;
    gap:12px;
}

footer{
    border-top:1px solid var(--line);
    padding:25px 6%;
    color:#5d6258;
    font-size:10px;
    display:flex;
    justify-content:space-between;
}

@media(max-width:800px){
    .login-grid{
        grid-template-columns:1fr;
    }

    .incident-row{
        grid-template-columns:70px 1fr;
    }

    .open-label{
        grid-column:2;
        justify-self:start;
    }
}
</style>
"""

LOGIN_PAGE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>VaultDesk | Secure Login</title>
    """ + STYLE + """
</head>

<body>

<header>
    <div class="brand">
        <div class="brand-mark">V</div>
        <div>
            <strong>VaultDesk</strong>
            <small>Asteria Incident Response</small>
        </div>
    </div>

    <div class="status">
        <span class="dot"></span>
        SECURE NODE ONLINE
    </div>
</header>

<div class="wrapper">

    <div class="label">VAULTDESK // AUTHENTICATION GATEWAY</div>

    <h1>Incident response<br>starts here.</h1>

    <p class="subtitle">
        Authorized Asteria Dynamics personnel only.
        Access is monitored and incident activity is logged.
    </p>

    <div class="panel">

        <div class="panel-inner login-grid">

            <div class="system-info">
                <div>NODE ........ <span>VD-01</span></div>
                <div>STATUS ...... <span>ONLINE</span></div>
                <div>NETWORK ..... INTERNAL</div>
                <div>ACCESS ...... AUTHENTICATED</div>
                <div>SESSION ..... ENCRYPTED</div>
            </div>

            <form method="post">

                <label>Username</label>
                <input name="username" autocomplete="username">

                <label>Password</label>
                <input name="password" type="password" autocomplete="current-password">

                <button type="submit">Authenticate →</button>

                {% if error %}
                <div class="error">{{ error }}</div>
                {% endif %}

            </form>

        </div>

    </div>

</div>

<footer>
    <span>© 2026 Asteria Dynamics</span>
    <span>VAULTDESK // INTERNAL USE ONLY</span>
</footer>

</body>
</html>
"""

DASHBOARD = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>VaultDesk | Incident Dashboard</title>
    """ + STYLE + """
</head>

<body>

<header>
    <div class="brand">
        <div class="brand-mark">V</div>
        <div>
            <strong>VaultDesk</strong>
            <small>Incident Response Console</small>
        </div>
    </div>

    <div class="status">
        <span class="dot"></span>
        SESSION ACTIVE
    </div>
</header>

<div class="wrapper">

    <div class="dashboard-top">

        <div>
            <div class="label">VAULTDESK // INCIDENT QUEUE</div>
            <h1>Active records.</h1>
        </div>

        <div class="userbox">
            AUTHENTICATED USER
            <strong>{{ username }}</strong>
        </div>

    </div>

    <p class="subtitle">
        Incident records currently assigned to your analyst account.
    </p>

    <div class="panel">

        <div class="incidents">

            {% for incident_id, incident in incidents %}

            <a class="incident-row"
               href="/vaultdesk/incident/{{ incident_id }}">

                <div class="incident-id">
                    #{{ incident_id }}
                </div>

                <div>
                    <div class="incident-title">
                        {{ incident.title }}
                    </div>

                    <div class="incident-meta">
                        ASSIGNED RECORD // ANALYST ACCESS
                    </div>
                </div>

                <div class="open-label">
                    OPEN RECORD →
                </div>

            </a>

            {% endfor %}

        </div>

    </div>

    <div class="actions">
        <a class="btn btn-outline" href="/vaultdesk/logout">
            Logout
        </a>
    </div>

</div>

<footer>
    <span>© 2026 Asteria Dynamics</span>
    <span>VAULTDESK // INCIDENT MANAGEMENT</span>
</footer>

</body>
</html>
"""

INCIDENT_PAGE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>VaultDesk | Incident {{ incident_id }}</title>
    """ + STYLE + """
</head>

<body>

<header>
    <div class="brand">
        <div class="brand-mark">V</div>
        <div>
            <strong>VaultDesk</strong>
            <small>Incident Response Console</small>
        </div>
    </div>

    <div class="status">
        <span class="dot"></span>
        RECORD OPEN
    </div>
</header>

<div class="wrapper">

    <div class="label">
        VAULTDESK // INCIDENT {{ incident_id }}
    </div>

    <h1>{{ incident.title }}</h1>

    <p class="subtitle">
        Asteria Dynamics incident investigation record.
    </p>

    <div class="incident-box">

        <div class="incident-head">
            <strong>Investigation Evidence</strong>
            <span>RECORD #{{ incident_id }}</span>
        </div>

        <pre>{{ incident.body }}</pre>

    </div>

    <div class="actions">

        <a class="btn btn-outline"
           href="/vaultdesk/dashboard">
            ← Back to Dashboard
        </a>

    </div>

</div>

<footer>
    <span>© 2026 Asteria Dynamics</span>
    <span>VAULTDESK // SECURE RECORD VIEWER</span>
</footer>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        user = USERS.get(username)

        if user and user["password"] == password:
            session["username"] = username
            return redirect(BASE + "/dashboard")

        error = "Invalid username or password"

    return render_template_string(LOGIN_PAGE, error=error)


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(BASE + "/")

    username = session["username"]

    visible_incidents = [
        (incident_id, incident)
        for incident_id, incident in INCIDENTS.items()
        if incident["owner"] == username
    ]

    return render_template_string(
        DASHBOARD,
        username=username,
        incidents=visible_incidents
    )


@app.route("/incident/<int:incident_id>")
def incident(incident_id):
    if "username" not in session:
        return redirect(BASE + "/")

    incident = INCIDENTS.get(incident_id)

    if not incident:
        abort(404)

    # Intentionally vulnerable for the CTF:
    # authenticated users can access any valid incident ID.
    return render_template_string(
        INCIDENT_PAGE,
        incident_id=incident_id,
        incident=incident
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(BASE + "/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)