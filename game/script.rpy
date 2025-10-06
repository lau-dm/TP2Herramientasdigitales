label capitulo_1:

    scene bg_denji_room with fade
    play music "audio/rain.ogg"

    show denji tired at center
    denji "Otra vez ese sueño. Otra vez esa sangre. ¿Qué parte de mí sigue siendo mía?"

    "La habitación es pequeña. El colchón está en el suelo. Pochita duerme a su lado, envuelto en una manta vieja."

    show pochita happy at left
    pochita "¿Tenés hambre, Denji?"

    show denji sad at center
    denji "Siempre tengo hambre. Pero ya ni sé si es físico o del otro."

    menu:
        "Salir a buscar trabajo":
            jump escena_bosque
        "Quedarse y hablar con Pochita":
            jump escena_confesion

label escena_bosque:

    scene bg_forest with fade
    play music "audio/tense_theme.ogg"

    "Denji camina por un sendero fangoso. Lo espera el cobrador de deudas."

    show yakuza angry at right
    yakuza "Hoy matás a un demonio. O te mato yo."

    show denji neutral at left
    denji "¿Y si no quiero?"

    yakuza "Entonces Pochita muere primero. ¿Querés eso?"

    menu:
        "Aceptar la misión":
            jump escena_demonio_zombi
        "Atacar al cobrador":
            "Denji intenta golpearlo, pero lo derriban. Lo arrastran al galpón igual."
            jump escena_demonio_zombi

label escena_confesion:

    scene bg_denji_room with fade
    play music "audio/soft_theme.ogg"

    show denji sad at center
    denji "Pochita... si muero, ¿podés vivir por mí?"

    show pochita serious at left
    pochita "Si vos morís, yo te doy mi corazón. Pero viví, Denji. Viví como vos querés."

    "Denji llora en silencio. Afuera, alguien golpea la puerta. Es el cobrador. Lo arrastran al galpón."

    jump escena_demonio_zombi

label escena_demonio_zombi:

    scene bg_warehouse with fade
    play music "audio/motorsaw.ogg"

    "Denji entra al galpón. Decenas de zombis lo rodean. El cobrador lo traicionó."

    show yakuza angry at right
    yakuza "Gracias por venir, perro. Ahora te convertís en comida."

    "Los zombis lo atacan. Pochita salta para protegerlo. Ambos caen. Sangre. Silencio."

    show denji weak at center
    denji "No quiero morir. No así."

    show pochita injured at left
    pochita "Viví tu sueño, Denji. Usá mi poder."

    "Fusión. La motosierra emerge de su pecho. Denji se levanta, transformado."

    show denji transformed at center
    denji "¡Ahora sí tengo hambre!"

    "Combate brutal. Cortes, gritos, sangre. Los zombis caen uno por uno."

    jump escena_makima

label escena_makima:

    scene bg_street_morning with fade
    play music "audio/soft_theme.ogg"

    "Denji despierta entre cadáveres. Una mujer lo observa."

    show makima calm at right
    makima "¿Sos humano o demonio?"

    show denji confused at left
    denji "No sé. Solo quiero desayuno."

    makima "Entonces sos útil. Vení conmigo."

    menu:
        "Aceptar sin preguntar":
            $ makima_confianza = True
            jump escena_auto
        "Preguntar quién es":
            $ makima_confianza = False
            jump escena_auto

label escena_auto:

    scene bg_car_interior with fade
    play music "audio/soft_theme.ogg"

    "Makima conduce. Denji mira por la ventana. El mundo parece distinto."

    show makima smile at right
    makima "¿Tenés nombre?"

    show denji tired at left
    denji "Denji. Y tengo hambre."

    makima "Entonces comé. Después, matás demonios para mí."

    "Denji muerde el pan. Llora sin que Makima lo note."

    jump escena_oficina

label escena_oficina:

    scene bg_office with fade
    play music "audio/tense_theme.ogg"

    "Makima presenta a Denji ante sus nuevos compañeros."

    show aki serious at left
    aki "No necesitamos perros."

    show power excited at right
    power "¡Yo quiero pelear con él! ¡Tiene cara de idiota!"

    show denji neutral at center
    denji "¿Esto es familia? ¿Esto es trabajo?"

    menu:
        "Responder con sarcasmo":
            $ power_confianza = True
            jump escena_rooftop
        "Callar y observar":
            $ aki_confianza = True
            jump escena_rooftop
        "Mirar a Makima":
            $ makima_confianza += 1
            jump escena_rooftop

label escena_rooftop:

    scene bg_rooftop with fade
    play music "audio/soft_theme.ogg"

    "Denji se sienta solo. Mira las estrellas. Pochita aparece en su mente."

    show pochita ghost at left
    pochita "¿Todavía querés ese sueño, Denji?"

    menu:
        "Sí. Aunque me destruya.":
            $ humanidad = False
            jump final_capitulo_1
        "No. Quiero algo real.":
            $ humanidad = True
            jump final_capitulo_1

label final_capitulo_1:

    scene black with fade
    play sound "audio/motorsaw.ogg"

    "Pantalla negra. Sonido de motosierra. Fin del capítulo 1."

    return