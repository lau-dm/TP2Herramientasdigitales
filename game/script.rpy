# script.rpy
define denji = Character("Denji", color="#f4c542")
define makima = Character("Makima", color="#e34234")
define aki = Character("Aki", color="#42a5f5")
define power = Character("Power", color="#ec407a")
define pochita = Character("Pochita", color="#ff7043")
define yakuza = Character("Yakuza", color="#999999")
define narrator = Character(None)


label start:

    jump prologo

label prologo:

    scene black with fade
    play music "audio/soft_theme.ogg"

    narrator "En este mundo, los miedos toman forma. El miedo a la oscuridad. El miedo a morir. El miedo a vivir."

    narrator "Y cuando el miedo se hace carne... nacen los demonios."

    narrator "Algunos los cazan por deber. Otros por poder. Y algunos... solo para sobrevivir."

    scene bg_denji_room with fade

    show denji tired at center
    denji "Mi nombre es Denji. Tengo dieciséis años. Y mi vida vale menos que un paquete de cigarrillos."

    show pochita happy at left
    pochita "Pero tienes a mí, Denji."

    denji "Sí, Pochita. Tú eres lo único que me queda."

    narrator "Denji vende partes de su cuerpo para pagar deudas. Un ojo. Un riñón. Un testículo."

    narrator "Su padre se suicidó. Su madre murió tosiendo sangre. Ahora vive en una choza húmeda con un demonio motosierra como mascota."

    denji "¿Crees que algún día viviremos bien? Comer pan con mermelada. Dormir en una cama limpia. Abrazar a alguien sin miedo."

    pochita "Si sueñas fuerte... tal vez."

    jump capitulo_1

label capitulo_1:

    scene bg_denji_room with fade
    play music "audio/rain.ogg"

    denji "Otra vez ese sueño. Otra vez esa sangre. ¿Qué parte de mí sigue siendo mía?"

    pochita "¿Tienes hambre, Denji?"

    denji "Siempre tengo hambre. Pero ya ni sé si es físico... o del otro."

    narrator "La habitación es pequeña. El colchón está en el suelo. El techo gotea. Afuera, la lluvia no cesa."

    menu:
        "Salir a buscar trabajo":
            jump escena_bosque
        "Quedarse y hablar con Pochita":
            jump escena_confesion

label escena_bosque:

    scene bg_forest with fade
    play music "audio/tense_theme.ogg"

    narrator "Denji camina por un sendero fangoso. Lo espera el cobrador de deudas."

    show yakuza angry at right
    yakuza "Hoy matas a un demonio. O te mato yo."

    show denji neutral at left
    denji "¿Y si no quiero?"

    yakuza "Entonces tu mascota muere primero. ¿Quieres eso?"

    denji "No... está bien. Lo haré."

    narrator "Lo llevan a un galpón abandonado. El aire huele a óxido y carne podrida."

    jump escena_demonio_zombi

label escena_confesion:

    scene bg_denji_room with fade
    play music "audio/soft_theme.ogg"

    denji "Pochita... si muero, ¿puedes vivir por mí?"

    pochita "Si tú mueres, yo te doy mi corazón. Pero vive, Denji. Vive como tú quieras."

    denji "Quiero comer pan con mermelada. Quiero abrazar a alguien. Quiero dormir sin miedo."

    narrator "Denji llora en silencio. Afuera, alguien golpea la puerta. Es el cobrador. Lo arrastran al galpón."

    jump escena_demonio_zombi

label escena_demonio_zombi:

    scene bg_warehouse with fade
    play music "audio/motorsaw.ogg"

    narrator "Denji entra al galpón. Decenas de zombis lo rodean. El cobrador lo traicionó."

    yakuza "Gracias por venir, perro. Ahora te conviertes en comida."

    denji "¡Pochita!"

    narrator "Los zombis lo atacan. Pochita salta para protegerlo. Ambos caen. Sangre. Silencio."

    denji "No quiero morir. No así."

    pochita "Vive tu sueño, Denji. Usa mi poder."

    narrator "Fusión. La motosierra emerge de su pecho. Denji se levanta, transformado."

    show denji transformed at center
    denji "¡Ahora sí tengo hambre!"

    narrator "Combate brutal. Cortes. Gritos. Sangre. Los zombis caen uno por uno."

    narrator "Denji no piensa. Solo corta. Solo sobrevive."

    jump escena_makima

label escena_makima:

    scene bg_street_morning with fade
    play music "audio/soft_theme.ogg"

    narrator "Denji despierta entre cadáveres. Una mujer lo observa."

    show makima calm at right
    makima "¿Eres humano o demonio?"

    show denji confused at left
    denji "No sé. Solo quiero desayuno."

    makima "Entonces eres útil. Ven conmigo."

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

    makima "¿Tienes nombre?"

    denji "Denji. Y tengo hambre."

    makima "Entonces come. Después, cazas demonios para mí."

    narrator "Denji muerde el pan. Llora sin que Makima lo note."

    denji "¿Esto es amor? ¿O solo otra cadena?"

    jump escena_oficina

label escena_oficina:

    scene bg_office with fade
    play music "audio/tense_theme.ogg"

    makima "Él es Denji. Es mío. Trátenlo bien."

    show aki serious at left
    aki "No necesitamos perros."

    show power excited at right
    power "¡Yo quiero pelear con él! ¡Tiene cara de idiota!"

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

    narrator "Denji se sienta en el techo. Mira las estrellas. Pochita aparece en su mente."

    pochita "¿Todavía quieres ese sueño, Denji?"

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

    narrator "Pantalla negra. Sonido de motosierra. Fin del capítulo 1."

    return

define denji = Character("Denji", color="#f4c542")
define makima = Character("Makima", color="#e34234")
define aki = Character("Aki", color="#42a5f5")
define power = Character("Power", color="#ec407a")
define pochita = Character("Pochita", color="#ff7043")
define narrator = Character(None)

default aki_confianza = 0
default power_confianza = 0
default humanidad = True

label capitulo_2:

    scene bg_car_interior with fade
    play music "audio/soft_theme.ogg"

    show denji tired at left
    show makima calm at right

    denji "¿Esto es Tokio? Nunca imaginé que fuera tan gris."

    makima "La ciudad no es gris. Solo depende de cómo la mires."

    denji "¿Y tú cómo la ves?"

    makima "Como un tablero. Y tú eres una pieza nueva."

    narrator "Denji no entiende. Pero le gusta cómo suena."

    makima "Hoy conocerás a tu compañero. No lo decepciones."

    jump escena_aki

label escena_aki:

    scene bg_street_day with fade
    play music "audio/rain.ogg"

    show aki serious at right
    show denji neutral at left

    aki "¿Este es el nuevo?"

    denji "Soy Denji. Tengo una motosierra en el pecho. ¿Eso cuenta?"

    aki "No me impresiona. Si no sirves, te saco yo mismo."

    narrator "Aki lo lleva por un callejón. Lo golpea sin previo aviso."

    denji "¡¿Qué te pasa?!"

    aki "Renuncia. No estás hecho para esto."

    menu:
        "Pelear con Aki":
            $ aki_confianza -= 1
            jump pelea_aki
        "Aguantar el golpe":
            $ aki_confianza += 1
            jump respeto_aki

label pelea_aki:

    narrator "Denji lo golpea. Aki lo derriba. Makima aparece."

    show makima neutral at center

    makima "¿Qué pasó?"

    aki "No sirve. Es un perro callejero."

    makima "Entonces vivirá contigo. Aprende a entrenarlo."

    narrator "Aki suspira. Denji sonríe con sangre en la boca."

    jump escena_departamento

label respeto_aki:

    narrator "Denji aguanta. No responde. Makima aparece."

    show makima neutral at center

    makima "¿Cómo fue?"

    aki "No sirve. Pero no se rinde."

    makima "Entonces vivirá contigo. Aprende a entenderlo."

    narrator "Aki frunce el ceño. Denji baja la cabeza."

    jump escena_departamento

label escena_departamento:

    scene bg_apartment with fade
    play music "audio/soft_theme.ogg"

    narrator "El departamento de Aki es limpio, ordenado, silencioso. Todo lo que Denji no es."

    show aki serious at right
    show denji neutral at left

    aki "No toques mis cosas. No hagas ruido. No molestes."

    denji "¿Y si quiero usar el baño primero?"

    aki "Entonces peleamos por eso."

    menu:
        "Responder con sarcasmo":
            $ aki_confianza -= 1
            jump escena_rutina
        "Pedir disculpas":
            $ aki_confianza += 1
            jump escena_rutina

label escena_rutina:

    scene bg_morning_tokyo with fade
    play music "audio/soft_theme.ogg"

    narrator "Días pasan. Denji aprende a limpiar, cocinar, patrullar. Pero no a entender a Aki."

    show denji neutral at center
    show aki serious at right

    denji "¿Por qué haces esto? ¿Por qué cazas demonios?"

    aki "Porque uno mató a mi familia. Y porque quiero matar a otro."

    denji "¿Y si no lo logras?"

    aki "Entonces muero intentándolo."

    narrator "Denji no responde. Pero algo en él cambia."

    jump escena_power

label escena_power:

    scene bg_office with fade
    play music "audio/tense_theme.ogg"

    show makima calm at center
    show power excited at right
    show denji surprised at left

    makima "Denji, conoce a tu nueva compañera."

    power "¡Soy Power! ¡Soy la mejor! ¡Tú eres mi sirviente!"

    denji "¿Qué clase de demonio eres?"

    power "¡Soy la Demonio de la Sangre! ¡Y tengo hambre!"

    makima "Ambos tienen demonios. Ambos serán juzgados por resultados."

    menu:
        "Aceptar trabajar con Power":
            $ power_confianza += 1
            jump escena_mision
        "Rechazarla":
            $ power_confianza -= 1
            jump escena_mision

label escena_mision:

    scene bg_street_night with fade
    play music "audio/motorsaw.ogg"

    narrator "Denji y Power patrullan juntos. Ella habla sin parar. Él solo escucha."

    show power excited at right
    show denji neutral at left

    power "¡Mi gato Nyako es más importante que tú! ¡Si algo le pasa, mato a todos!"

    denji "¿Tienes un gato?"

    power "¡Sí! ¡Y lo amo más que a la humanidad!"

    narrator "Denji sonríe. Por primera vez, siente que no está solo."

    menu:
        "Contarle sobre Pochita":
            $ power_confianza += 1
            jump escena_final_2
        "Guardar silencio":
            jump escena_final_2

label escena_final_2:

    scene bg_rooftop with fade
    play music "audio/soft_theme.ogg"

    narrator "Denji se sienta en el techo. Mira la ciudad. Piensa en Makima, Aki y Power."

    show denji neutral at center
    show pochita ghost at left

    denji "¿Esto es suerte? ¿O solo otra cadena?"

    pochita "Vive tu sueño, Denji. Pero no olvides quién eres."

    menu:
        "Seguir el sueño sin pensar":
            $ humanidad = False
            return
        "Buscar algo real":
            $ humanidad = True
            return