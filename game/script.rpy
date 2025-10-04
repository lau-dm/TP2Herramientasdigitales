# script.rpy

label start:
    jump cap1_start

# =========================
# VARIABLES INICIALES
# =========================
default humanidad = 0
default violencia = 0
default lealtad_corp = 0
default camino = ""

# =========================
# DEFINICIÓN DE PERSONAJES
# =========================
define d = Character("David", color="#FFD700")
define gloria = Character("Gloria", color="#FF9999")
define yumi = Character("Yumi", color="#99CCFF")
define rex = Character("Rex", color="#FF6600")
define teacher = Character("Profesora Arasaka", color="#CCCCCC")

# =========================
# ESCENARIOS
# =========================
image bg_nightcity_district = "images/bg_nightcity_district.jpg"
image bg_classroom_arasaka = "images/bg_classroom_arasaka.jpg"

# =========================
# PERSONAJES VISUALES
# =========================
image gloria worried = "images/gloria_worried.png"
image yumi neutral = "images/yumi_neutral.png"
image rex smug = "images/rex_smug.png"
image teacher_arasaka = "images/teacher_arasaka.png"

# =========================
# CAPÍTULO 1
# =========================
label cap1_start:

    scene bg_nightcity_district with fade
    play music "music/nightcity_loop.ogg" fadein 1.0

    "Night City nunca duerme. Pero para los que no tenemos dinero, tampoco perdona."
    "Soy David Martínez. Hoy es mi primer día en la prestigiosa Academia Arasaka."
    "Mamá cree que este es el comienzo de algo grande, pero yo sé lo que significa vivir en las calles: nadie te espera si caes."

    show gloria worried at left with dissolve
    gloria "David… recuerda comer algo antes de entrar, no llegues muerto de hambre como siempre."
    d "Lo sé, mamá. Estoy bien."
    gloria "Solo cuida tu espalda, cariño. No todos aquí son gente decente."
    d "(Lo sé… y aún así, debo hacerlo.)"

    "El camino hasta la entrada principal es un caos de hologramas, anuncios de ciberimplantes y drones patrullando el área."
    "No hay margen de error. En Arasaka, la perfección es una obligación, y cualquier fallo puede costarte caro."

    show yumi neutral at right with dissolve
    yumi "¡Eh, David! Llegas justo a tiempo… aunque no sé si para bien o para mal."
    d "Yumi… vaya, ya veo que estás igual de sarcástica que siempre."
    yumi "Aprenderás rápido que en esta ciudad, los que no se adaptan, se quedan atrás."
    d "Eso lo sé demasiado bien…"

    menu:
        "¿Cómo responde David?"
        "Con orgullo y confianza":
            $ humanidad += 1
            d "No vine aquí para ser uno más. Estoy listo para demostrar lo que valgo."
            yumi "Mm… veremos cuánto dura tu valentía."
        "Con cautela, evaluando la situación":
            d "Haré lo que pueda… necesito observar primero."
            $ humanidad += 0
            yumi "Observador, eh… me gusta eso. Pero no por mucho."
        "Con enojo, impaciente":
            $ violencia += 1
            d "¡Solo quiero entrar y empezar! No necesito charlas."
            yumi "Calma, Martínez… nadie aquí tolera impulsos tontos."

    scene bg_classroom_arasaka with fade
    play music "music/academia_loop.ogg" fadein 1.0

    "El aula está llena de estudiantes con implantes recién estrenados, trajes corporativos y chips de datos parpadeando en sus muñecas."
    "Rex Arasaka, el hijo del ejecutivo que supervisa esta generación, me lanza una mirada desde su asiento."

    show rex smug at right with dissolve
    rex "Así que tú eres David Martínez… he oído de ti. Vamos a ver si eres digno de Arasaka."
    d "(Su mirada me pesa… pero no puedo mostrar miedo.)"

    menu:
        "¿Cómo responder a Rex?"
        "Con firmeza, sin miedo":
            $ lealtad_corp -= 1
            d "No vine aquí a complacer a nadie. Aprenderé a mi manera."
            rex "Interesante… arrogancia, pero veremos si sirve para algo."
        "Con sumisión estratégica":
            $ lealtad_corp += 1
            d "Espero poder estar a la altura… aprenderé de los mejores."
            rex "Bien. Al menos eres inteligente."
        "Con sarcasmo":
            $ humanidad += 1
            d "¿Dignidad Arasaka? Suena más a publicidad."
            rex "¡Ja! Otro que piensa que es gracioso… veremos hasta cuándo."

    show teacher_arasaka at center with dissolve
    teacher "Bienvenidos a la Academia Arasaka. Este año será distinto… exigiremos lo mejor de ustedes."
    teacher "Recuerden: aquí, cada decisión que tomen afectará su futuro. Cada error será recordado."

    "Un escalofrío recorre mi espalda. Las palabras de la profesora no son solo formalidades: son advertencias."

    "Durante el recreo, veo a un estudiante más joven siendo intimidado por un grupo de compañeros con implantes visibles y armas de entrenamiento."

    menu:
        "¿Qué hace David?"
        "Intervenir y ayudar al estudiante":
            $ humanidad += 2
            "David se acerca y enfrenta al grupo, obligándolos a retroceder."
            yumi "¡Eso estuvo bien! No todos harían eso."
            rex "¡Bah! Inútil… eso no ayuda a nadie."
        "Ignorar y seguir su camino":
            $ humanidad -= 1
            "David decide no involucrarse. No es su problema."
            yumi "(Suspiro) A veces eres demasiado frío."
        "Tomar ventaja de la situación":
            $ violencia += 1
            "David empuja al líder del grupo y se gana respeto inmediato, aunque despierta enemistad."
            rex "Hmm… ese chico tiene agallas… y problemas en puerta."

    # Evaluación del camino
    if humanidad > violencia and humanidad > lealtad_corp:
        $ camino = "calle"
    elif lealtad_corp > humanidad and lealtad_corp > violencia:
        $ camino = "corporación"
    else:
        $ camino = "caos"

    "El día termina con más preguntas que respuestas. Night City se extiende bajo un cielo de neón, recordándome que cada decisión que tome me acercará a la calle, a la corporación, o a la perdición."

    jump cap2_start