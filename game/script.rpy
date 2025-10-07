# CHAINSAW MAN: SANGRE Y ENGRANAJES
# Proyecto TP2 - Novela Visual
# Autor: [Joaquin]
# Idioma: Español

# Declaración de personajes
define d = Character("Denji", color="#FF5C5C")
define m = Character("Makima", color="#FFB6C1")
define p = Character("Power", color="#FF7070")
define a = Character("Aki", color="#9AD0EC")
define po = Character("Pochita", color="#FFA500", what_prefix="(", what_suffix=")")
define narrador = Character(None, kind=narrator)

# Fondo y música inicial
label start:

    scene bg_city_ruins
    play music "theme_intro.mp3" fadein 1.5
    with fade

    narrador "Tokio. Años después de la gran guerra entre humanos y demonios."
    narrador "Los cazadores de demonios sobreviven entre ruinas y miedo."
    d "Otro día, otra cabeza que cortar. Ya ni sé por qué sigo haciéndolo..."
    po "Denji... ¿aún recuerdas tu sueño?"
    d "¿Pochita...? Hace tiempo que no te oía."

    scene bg_office_night with dissolve
    play sound "door_open.mp3"

    m "Denji. Tengo una nueva misión para ti."
    d "¿Otra más? Apenas me queda gasolina."
    m "Un demonio desconocido apareció al norte. Es una amenaza de nivel especial."
    m "Confío en que harás lo correcto, como siempre."
    d "..."
    d "¿Y si no quiero?"
    m "Entonces morirás. Pero morirías con propósito."

    menu:
        "¿Qué hará Denji?":
            "Obedecer a Makima":
                jump obedecer
            "Desobedecer la orden":
                jump desobedecer
            "Buscar venganza personal":
                jump venganza

# ====== RAMA 1 =======
label obedecer:

    scene bg_warehouse_dark
    play music "mission.mp3" fadein 1.0
    with fade

    d "Está bien, Makima. Pero Power viene conmigo."
    m "Haz lo que quieras. Solo tráeme el corazón del demonio."

    p "¡Sí! ¡Sangre, tripas y gloria!"
    d "No sé por qué sigo dejándome arrastrar por ti..."
    narrador "Ambos entran al almacén. Un rugido demoníaco retumba."

    play sound "chainsaw_on.mp3"
    d "¡Vamos allá!"

    menu:
        "En medio del combate...":
            "Confiar en Makima y seguir órdenes":
                jump obedecer_makima
            "Dudar y proteger a Power":
                jump obedecer_power

label obedecer_makima:
    scene bg_hell_gate
    play music "betrayal.mp3" fadein 1.0
    with fade

    narrador "El demonio cae. Pero la energía de Makima se apodera del aire."
    m "Buen trabajo, Denji. Ahora... entrégame tu corazón."
    d "¿Qué...?"
    m "Siempre fue mi objetivo. El contrato se cumple ahora."
    play sound "heartbeat.mp3"
    d "No... ¡No!"
    narrador "El mundo se oscurece. Denji se convierte en el arma final de Makima."
    jump final1

label obedecer_power:
    scene bg_warehouse_dark
    p "¡Denji, cuidado!"
    play sound "fight.mp3"
    narrador "Power salta frente a él, recibiendo el golpe fatal."
    d "¡Power, no!"
    p "Tú... corta su cabeza por mí..."
    d "..."
    play sound "chainsaw_on.mp3"
    narrador "Denji destruye al demonio, pero su furia lo consume."
    jump final2

# ====== RAMA 2 =======
label desobedecer:

    scene bg_city_ruins
    with fade
    d "No pienso seguir tus órdenes, Makima."
    m "Eso es... decepcionante, Denji."
    a "Te estás jugando la vida, Denji."
    d "La vida nunca me dio nada, Aki."
    a "Entonces déjame ayudarte, por última vez."

    menu:
        "¿Aceptar ayuda de Aki?":
            "Sí, trabajar juntos":
                jump desobedecer_aki
            "No, hacerlo solo":
                jump desobedecer_solo

label desobedecer_aki:
    play music "mission.mp3"
    scene bg_city_night
    narrador "Ambos se enfrentan al demonio del vacío."
    play sound "fight.mp3"
    a "¡Ahora, Denji!"
    d "¡Toma esto!"
    play sound "explosion.mp3"
    narrador "El demonio cae. Pero Aki está herido de muerte."
    a "Al menos... esta vez... no fallamos."
    d "No..."
    jump final3

label desobedecer_solo:
    play music "betrayal.mp3"
    scene bg_hell_gate
    narrador "Denji se lanza solo al combate. Pero algo dentro de él despierta."
    po "Demasiada sangre... demasiada rabia..."
    play sound "heartbeat.mp3"
    d "¡POOOCHITA!"
    narrador "Su humanidad desaparece. Solo queda la motosierra."
    jump final4

# ====== RAMA 3 =======
label venganza:

    scene bg_office_night
    with dissolve
    d "No más órdenes. No más mentiras."
    p "Denji, ¿qué haces?"
    d "Lo que debí hacer desde el principio: cortar la cabeza del sistema."
    p "Eso suena... ¡divertido!"

    menu:
        "Durante el ataque a la sede...":
            "Perdonar a Power cuando te traiciona":
                jump venganza_perdonar
            "Matar a Power":
                jump venganza_matar

label venganza_perdonar:
    scene bg_dawn
    play music "ending_light.mp3"
    narrador "Denji baja su motosierra."
    d "No puedo seguir matando a quienes me importan."
    p "Idiota... yo solo tenía miedo..."
    narrador "Ambos se enfrentan a Makima juntos, liberando a los demonios esclavizados."
    d "Si este es el final, que sea libre."
    jump final5

label venganza_matar:
    scene bg_hell_gate
    play music "ending_dark.mp3"
    play sound "chainsaw_on.mp3"
    narrador "Denji corta a Power sin dudar."
    d "El amor solo me hizo débil."
    narrador "Los demonios se arrodillan ante él. El mundo tiembla."
    m "Bienvenido... nuevo rey de los demonios."
    jump final6

# ====== FINALES ======

label final1:
    scene bg_hell_gate
    stop music fadeout 2.0
    narrador "Final 1: El Corazón de Makima — Denji se convierte en su arma definitiva."
    return

label final2:
    scene bg_dawn
    narrador "Final 2: Huida — Denji sobrevive, pero Power muere. Su humanidad se desvanece."
    return

label final3:
    scene bg_city_ruins
    narrador "Final 3: Sacrificio — Aki muere, pero Denji vence al demonio. El costo es eterno."
    return

label final4:
    scene bg_hell_gate
    narrador "Final 4: El Demonio Interior — Denji pierde su alma y destruye todo a su paso."
    return

label final5:
    scene bg_dawn
    narrador "Final 5: Liberación — Denji y Power liberan a los demonios del control humano."
    return

label final6:
    scene bg_hell_gate
    narrador "Final 6: Señor de los Demonios — Denji reina sobre un mundo destruido."
    return
