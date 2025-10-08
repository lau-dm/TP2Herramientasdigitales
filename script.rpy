# -------------------------
# DEFINICIÓN DE PERSONAJES CON COLORES
# -------------------------
define denji = Character("Denji", color="#FFD700")
define pochita = Character("Pochita", color="#FF8C00")
define power = Character("Power", color="#FF4500")
define aki = Character("Aki", color="#1E90FF")
define makima = Character("Makima", color="#FF69B4")
define demonio = Character("Demonio", color="#8B0000")
define demonio_nuevo = Character("Demonio Nuevo", color="#880000")
define civil = Character("Civil", color="#AAAAAA")
define panero = Character("Panero", color="#C2B280")
define yakuza = Character("Yakuza", color="#444444")

# -------------------------
# INICIO
# -------------------------
label introduccion:
    scene city_rooftop_night
    with fade
    play music "intro_theme.ogg" fadein 2.0
    "La noche cae sobre la ciudad, las luces de neón parpadean entre la lluvia y el eco de sirenas lejanas. Denji observa el horizonte, sintiendo el peso de sus sueños y cicatrices."
    "Pochita se acurruca a su lado, el único amigo que nunca lo ha traicionado. Power se burla desde el borde del tejado, mientras Aki afila su espada en silencio. Makima, distante, contempla la ciudad como si todo estuviera bajo su control."
    denji "¿Alguna vez podré vivir una vida normal? El pan con mermelada parece tan lejano..."
    pochita "No pierdas la esperanza, Denji. Incluso en la oscuridad, hay luz."
    power "¡Deja de soñar y prepárate para pelear! Si te distraes, te comen vivo."
    aki "La ciudad nunca duerme, y los demonios tampoco. Mantente alerta."
    makima "Cada decisión que tomes puede cambiar tu destino, Denji. Observa, aprende y actúa."
    "Un trueno sacude el cielo. Denji recuerda los días en que luchaba solo por sobrevivir, vendiendo partes de su cuerpo para pagar deudas. Ahora tiene aliados, pero el peligro es mayor que nunca."
    "¿Estás listo para enfrentarte a demonios, descubrir secretos y forjar tu propio camino? El destino de todos está en tus manos."
    menu:
        "Comenzar la historia principal":
            jump start
        "Ver menú de rutas secretas":
            jump menu_rutas_secretas

label start:
    scene city_rooftop_night
    with fade
    play music "rainy_night.ogg" fadein 2.0
    "La ciudad está cubierta de sombras, la lluvia golpea los techos y el aire huele a metal y miedo. Los gritos de demonios se mezclan con el retumbar de truenos, creando una atmósfera opresiva."
    denji "Otro día más, otro demonio… ¿por qué siempre yo?"
    aki "¿No dormiste bien, Denji? Pareces más cansado que de costumbre."
    denji "No mucho... soñé que tenía una casa, un colchón y una sábana limpia. Pero al despertar, solo tenía a Pochita y el ruido de la ciudad."
    pochita "¡Eso es mejor que nada! Yo prefiero estar contigo que en cualquier mansión."
    power "¡Bah! Los sueños son para los débiles. Yo solo sueño con sangre y pan."
    denji "¿Nunca has querido algo más, Power?"
    power "¿Más que pan? Imposible. Bueno, tal vez un trono de huesos."
    aki "No le hagas caso, Denji. Power solo sabe bromear. Pero... ¿qué harías si pudieras elegir tu vida?"
    denji "No sé... tal vez solo vivir tranquilo, sin miedo. Comer pan con mermelada y dormir sin pensar en demonios."
    makima "La tranquilidad es un lujo en nuestro mundo. Pero a veces, los sueños nos mantienen vivos."
    "Un relámpago ilumina la ciudad. De repente, un demonio con brazos como látigos de acero emerge de un callejón, su silueta distorsionada por la lluvia y la luz de neón."
    demonio "¡Intrusos! ¡Vuestra sangre será mía!"
    denji "Maldita sea… ¡Vamos allá! No puedo dejar que el miedo me paralice. Pero, ¿y si hoy sí me matan?"
    pochita "¡Vamos juntos, Denji! Recuerda lo que te prometiste: nunca retroceder. Y si te matan, ¡te revivo a mordidas!"
    power "¡Cuidado con los brazos! Si te alcanza, no habrá segunda oportunidad. Aunque si mueres, ¿puedo quedarme con tu pan?"
    aki "Analiza su patrón de ataque. Busca su debilidad, no te precipites. Y si ves que Power se lanza primero, ¡agáchate!"
    makima "Confía en tus instintos, pero no ignores a tus amigos. Y si todo falla, improvisa."
    show screen rain_overlay
    "El sonido de la motosierra de Denji se mezcla con la lluvia, creando una sinfonía de caos. El grupo se prepara para enfrentar el peligro, cada uno con sus propios miedos y esperanzas. Power sonríe con arrogancia, Aki afila su espada, Makima observa con una calma inquietante, y Pochita se acomoda en el hombro de Denji, listo para saltar si es necesario."
    "Antes de actuar, Denji recuerda una promesa que hizo a Pochita: nunca dejar que el miedo lo controle. El grupo intercambia miradas, sabiendo que cada batalla puede ser la última."
    aki "Denji, pase lo que pase, no te separes del grupo."
    power "¡Y si te separas, grita fuerte! Así sabremos dónde recoger tus pedazos."
    denji "Gracias por el apoyo, Power... creo."
    makima "Recuerden, cada uno tiene un papel. No subestimen el poder de la amistad."
    pochita "¡Y el poder del pan!"
    menu:
        "¿Qué haces?":
            "Atacar directamente (¡A lo Chainsaw Man!)":
                jump rama_1_a
            "Huir y buscar aliados (¿Cobarde o estratega?)":
                jump rama_2_a
            "Negociar con demonio (¿Y si funciona?)":
                jump rama_3_a
            "Observar y esperar (Modo ninja)":
                jump rama_4_a
            "Investigar sonido extraño cercano (¿Curiosidad o problema?)":
                jump rama_5_a
            "Preguntar a Power por un consejo (¿Sabio o peligroso?)":
                jump consejo_power
            "Investigar la División Especial (¿Secretos ocultos?)":
                jump rama_6_division
            "Seguir a Makima en secreto (¿Espionaje?)":
                jump rama_7_espionaje
            "Buscar el origen de Pochita (¿Misterio profundo?)":
                jump rama_8_origen_pochita
            "Entrar a la tienda de sangre (¿Recompensa o peligro?)":
                jump rama_9_tienda_sangre

label consejo_power:
    power "¿Mi consejo? ¡Golpéalo en la cara y grita mucho! Si no funciona, corre y déjaselo a Aki."
    aki "No le hagas caso, Denji. Power solo quiere ver el caos."
    pochita "¡Yo apoyo el caos! Pero con cuidado."
    makima "A veces el caos revela la verdad. Pero no abuses."
    "Power te guiña un ojo y te empuja hacia el demonio. ¿Sigues su consejo o prefieres otra opción?"
    menu:
        "¿Qué decides?":
            "Seguir el consejo de Power (¡A lo loco!)":
                jump rama_1_a
            "Pensar mejor las cosas":
                jump start

# -------------------------
# RAMA 1 – ATAQUE DIRECTO
# -------------------------
label rama_1_a:
    scene city_night_rain
    with fade
    play sound "chainsaw_start.ogg"

    "La lluvia arrecia, el suelo resbala bajo los pies de Denji. El demonio se mueve con rapidez, sus látigos cortan el aire y salpican agua y sangre."
    denji "¡No puedo dejar que lastime a nadie más! Aunque el miedo me carcoma, debo avanzar."
    power "¡Denji, cuidado! ¡Ese demonio es enorme! Si caes, no habrá quien te salve. Pero si lo derrotas, ¡te invito a mi sangre favorita!"
    aki "Nos respaldamos, ve con todo! Pero no pierdas la cabeza, la fuerza sin control es destrucción. Si te lanzas sin pensar, Makima te va a regañar."
    makima "Denji, controla tu fuerza o destruirás todo a tu alrededor. Recuerda lo que te enseñé. Observa, aprende y actúa."
    pochita "¡Sígueme, Denji! ¡Yo te cubro! No estás solo en esto. Si te caes, te levanto a mordidas."

    "Denji activa la motosierra, cortando el aire con un zumbido metálico. El rugido de la máquina es un grito de guerra, y la lluvia intensifica la escena, el reflejo de luces de neón crea destellos sobre charcos de agua."
    "El demonio lanza un golpe, pero Denji logra esquivarlo, dejando marcas profundas en las paredes. El corazón de Denji late con fuerza, cada segundo puede ser el último."
    "Power y Aki se posicionan a los lados, listos para intervenir. Makima observa desde la distancia, su mirada es fría y calculadora."
    "De repente, Power salta sobre el demonio, gritando:"
    power "¡Por el poder de Power!"
    "El demonio la esquiva y lanza un látigo hacia Denji, que apenas logra bloquearlo con la motosierra."
    aki "¡Denji, cubre tu flanco!"
    "Pochita salta y muerde el látigo, dándole a Denji una oportunidad."
    pochita "¡Ahora, Denji!"
    "Makima sonríe levemente, como si todo estuviera bajo control."

    menu:
        "¿Cómo atacas?":
            "Ataque frontal con motosierra":
                jump rama_1_b
            "Ataque combinado con Power":
                jump rama_1_power_combo
            "Distracción de Aki y ataque sorpresa":
                jump rama_1_aki_sorpresa
            "Dejar que Pochita actúe primero":
                jump rama_1_pochita
            "Intentar impresionar a Makima":
                jump rama_1_makima

label rama_1_power_combo:
    "Denji y Power coordinan un ataque, Power lanza escombros y Denji se lanza con la motosierra."
    power "¡Ahora, Denji! ¡Hazlo sangrar!"
    denji "¡Vamos juntos!"
    "El demonio recibe el impacto, pero se enfurece y lanza ambos contra una pared."
    aki "¡No bajen la guardia!"
    "Makima observa, sin intervenir."
    menu:
        "¿Qué haces tras el golpe?":
            "Levantarse y atacar juntos":
                jump rama_1_b
            "Dejar que Power distraiga y atacar por detrás":
                jump rama_1_c

label rama_1_aki_sorpresa:
    "Aki usa su espada y crea una cortina de humo. Denji aprovecha y ataca por sorpresa."
    aki "¡Ahora, Denji!"
    denji "¡Gracias, Aki!"
    "El demonio queda herido, pero lanza un látigo hacia Aki."
    power "¡Cuidado, Aki!"
    "Pochita salta y muerde el látigo, salvando a Aki."
    menu:
        "¿Quién ataca ahora?":
            "Denji":
                jump rama_1_b
            "Power":
                jump rama_1_power_combo

label rama_1_pochita:
    "Pochita se transforma y ataca al demonio, sorprendiendo a todos."
    pochita "¡Por Denji!"
    "El demonio retrocede, pero se enfurece y lanza un ataque masivo."
    denji "¡Pochita, cuidado!"
    "Makima interviene con su poder, deteniendo el ataque."
    makima "No subestimen a sus enemigos."
    menu:
        "¿Quién lidera el siguiente ataque?":
            "Denji":
                jump rama_1_b
            "Makima":
                jump rama_1_makima

label rama_1_makima:
    "Denji intenta impresionar a Makima con un ataque espectacular, girando la motosierra y lanzándose al demonio."
    denji "¡Esto es para ti, Makima!"
    makima "No busques mi aprobación, busca sobrevivir."
    "El demonio esquiva y lanza a Denji contra el suelo. Power se ríe."
    power "¡Eso te pasa por presumido!"
    aki "Concéntrate, Denji."
    menu:
        "¿Qué haces ahora?":
            "Ataque frontal":
                jump rama_1_b
            "Ataque combinado":
                jump rama_1_power_combo

label rama_1_b:
    "Denji lanza un ataque completo, cortando el aire mientras el demonio retrocede."
    demonio "¡GRRAAAHH!"
    power "¡Cuidado con su cola!"
    aki "¡No lo dejes escapar!"
    pochita "¡Estoy contigo, Denji!"

    "De repente, un demonio menor salta desde un edificio cercano."
    demonio "¡Grrr!"
    denji "¡Otra vez no!"
    power "¡Denji, tenemos que dividirnos!"
    aki "Plan B, rápido."
    pochita "¡Cúbreme mientras atacas!"

    menu:
        "¿Persigues al demonio principal o eliminas al menor primero?":
            "Principal":
                jump rama_1_b_principal
            "Menor":
                jump rama_1_b_menor

label rama_1_b_principal:
    "Denji se concentra en el demonio principal. Power y Aki eliminan al menor."
    denji "¡No me detengo hasta que caiga!"
    pochita "¡Vamos juntos!"
    "El demonio principal cae finalmente, Denji exhausto pero victorioso."

    menu:
        "¿Recuperarte solo o con Power?":
            "Solo":
                jump rama_1_final_1
            "Con Power":
                jump rama_1_final_2

label rama_1_b_menor:
    "El demonio menor es eliminado rápidamente, pero el principal aprovecha la distracción."
    demonio "¡Jajajaja! ¡Vais a morir!"
    denji "¡Maldita sea!"
    power "¡Tenemos que reagruparnos!"
    aki "¡Plan B, Denji!"
    pochita "¡Cuidado, Denji!"
    jump rama_1_final_3

label rama_1_c:
    "Herimos parcialmente al demonio, que retrocede entre las sombras."
    denji "Volverá más fuerte…"
    power "¡Podemos atraparlo juntos!"
    aki "O lo dejamos y planeamos mejor."
    pochita "Yo puedo ayudar a cubrirte."

    menu:
        "¿Persigues o te refugias?":
            "Persigues":
                jump rama_1_final_4
            "Refugiarse":
                jump rama_1_final_5

# -------------------------
# RAMA 2 – HUIR Y BUSCAR ALIADOS
# -------------------------
label rama_2_a:
    scene city_dark_streets
    with fade
    play music "escape.ogg" fadein 1.0

    "Denji corre por calles oscuras y llenas de escombros, el sonido de sus pasos se mezcla con el eco de explosiones lejanas. La lluvia le dificulta la visión, pero el miedo lo impulsa a seguir adelante."
    denji "¿Estoy huyendo o planeando? Tal vez solo soy un cobarde con suerte..."
    power "¡Por aquí, Denji! Si te caes, te dejo atrás. Pero si llegas primero, te doy mi postre."
    aki "No nos separes. Cada segundo cuenta. Si Power te ofrece comida, desconfía."
    pochita "¡Denji, confía en mí! Si te pierdes, ladro fuerte."
    "De repente, Denji tropieza con una caja y casi cae. Power se ríe, Aki lo ayuda a levantarse."
    power "¡Eso fue patético!"
    aki "Concéntrate, Denji."
    "Un ruido extraño se escucha en un callejón cercano. ¿Aliado o enemigo?"

    menu:
        "¿A quién buscas primero?":
            "Power (confías en su fuerza y locura)":
                jump rama_2_b
            "Aki (prefieres estrategia y calma)":
                jump rama_2_c
            "Buscar a Makima (¿protección o peligro?)":
                jump rama_2_makima
            "Seguir a Pochita (¿intuición canina?)":
                jump rama_2_pochita
            "Investigar el ruido (¿curiosidad o problema?)":
                jump rama_2_ruido

label rama_2_makima:
    "Denji busca a Makima entre las sombras. La encuentra observando la batalla desde un edificio alto."
    makima "¿Huyes, Denji? A veces la retirada es la mejor estrategia. Pero no olvides por qué luchas."
    denji "Makima... ¿me ayudas?"
    makima "Solo si demuestras que lo mereces."
    menu:
        "¿Qué haces?":
            "Pedir ayuda directamente":
                jump rama_2_final_2
            "Intentar impresionar a Makima":
                jump rama_2_final_1

label rama_2_pochita:
    "Denji sigue a Pochita, que olfatea el aire y lo guía por un laberinto de callejones."
    pochita "¡Por aquí! Huele a demonio... y a pan."
    denji "¿Pan? ¿En serio?"
    power "¡Si hay pan, yo quiero!"
    "Encuentran a un demonio menor robando comida. Power lo ataca sin pensarlo."
    power "¡Mi pan!"
    "Aki suspira y ayuda a Denji a derrotar al demonio."
    menu:
        "¿Qué haces tras la pelea?":
            "Comer pan con Power":
                jump rama_2_final_1
            "Seguir buscando aliados":
                jump rama_2_c

label rama_2_ruido:
    "Denji investiga el ruido y encuentra a un civil escondido."
    denji "¿Estás bien?"
    "El civil le entrega información sobre el demonio principal."
    civil "Dicen que teme al fuego."
    aki "Eso puede ser útil."
    power "¿Fuego? ¡Yo puedo prender algo!"
    menu:
        "¿Usar la información o ignorarla?":
            "Usar fuego en el combate":
                jump rama_2_final_3
            "Ignorar y seguir buscando aliados":
                jump rama_2_b

label rama_2_b:
    "Power se une a Denji y ambos planean un ataque estratégico."
    power "¡Denji! Esta vez vamos juntos."
    denji "¡Perfecto!"
    aki "Si seguimos así, podremos derribarlo rápido."
    pochita "¡Yo cubro la retaguardia!"

    "Una explosión sacude la calle: un demonio bomba aparece."
    demonio "¡Boom!"
    denji "¡Cuidado!"
    power "¡Esquiva!"
    aki "¡Debemos reagruparnos!"
    pochita "¡Denji, rápido!"

    menu:
        "Cooperar o pelear separados?":
            "Cooperar":
                jump rama_2_final_1
            "Pelea separada":
                jump rama_2_final_2

label rama_2_c:
    "Aki llega y propone un ataque sigiloso."
    aki "Debemos mantenernos ocultos y atacar cuando menos lo esperen."
    denji "¡Entendido!"
    power "Espero que esto funcione…"
    pochita "¡Denji, vamos a sorprenderlos!"

    menu:
        "Sigilo o ataque frontal?":
            "Sigilo":
                jump rama_2_final_3
            "Frontal":
                jump rama_2_final_4

label rama_3_a:
    scene alley_dark
    with fade
    play music "tension.ogg" fadein 1.0

    "Denji se acerca al demonio con cautela, la lluvia cae entre los dos como una cortina de incertidumbre."
    denji "Tal vez pueda hablar con él… aunque Power diría que es una locura."
    pochita "¡Denji, sé cuidadoso! Si te come, no podré salvarte esta vez."
    power "¿Hablar con un demonio? ¿Estás loco? Mejor grítale y corre."
    aki "Analiza sus movimientos mientras hablas. Si ves que se pone nervioso, prepárate para atacar."
    demonio "¿Hablas o solo vienes a morir? Nadie negocia con el miedo."
    makima "Observa y aprende, Denji. Cada palabra importa. Pero recuerda, los demonios no siempre cumplen su palabra."

    "El demonio se acerca, sus ojos brillan con curiosidad y hambre. Denji siente el peso de la decisión."
    menu:
        "¿Cómo negocias?":
            "Intentar persuadirlo con promesas":
                jump rama_3_b
            "Amenazarlo con la motosierra":
                jump rama_3_c
            "Ofrecerle algo a cambio":
                jump rama_3_ofrecer_algo
            "Engañarlo con información falsa":
                jump rama_3_engano
            "Pedirle que se una al equipo (¡A lo Power!)":
                jump rama_3_unir_equipo

label rama_3_ofrecer_algo:
    denji "¿Qué tal si te doy algo a cambio de tu retirada?"
    demonio "¿Qué puedes ofrecerme, humano?"
    menu:
        "¿Qué ofreces?":
            "Comida humana":
                jump rama_3_final_1
            "Información sobre otros demonios":
                jump rama_3_final_3
            "Un favor futuro":
                jump rama_3_final_1
            "Nada, era broma":
                jump rama_3_c

label rama_3_engano:
    denji "Si no te vas, vendrá Makima y te convertirá en su mascota."
    demonio "¿Makima? ... Mejor me voy antes de que me encuentre."
    power "¡Eso sí que funcionó!"
    aki "A veces el miedo es la mejor arma."
    jump rama_3_final_3

label rama_3_unir_equipo:
    denji "¿Por qué no te unes a nosotros? Power dice que los equipos son más divertidos."
    power "¡Sí! ¡Más caos!"
    demonio "¿Unirme a humanos? ... Solo si me dan pan."
    pochita "¡Yo comparto mi pan!"
    "El demonio acepta y se une al grupo, aunque todos desconfían."
    jump rama_3_final_1

label rama_3_b:
    denji "No necesitamos pelear… podemos llegar a un acuerdo."
    pochita "¡Sí, Denji, mantén la calma!"
    demonio "Hmmm… interesante…"
    aki "Sigue con cuidado, Denji."
    menu:
        "¿Ofreces algo a cambio o pides información?":
            "Ofrecer":
                jump rama_3_final_1
            "Pedir información":
                jump rama_3_final_3

label rama_3_c:
    denji "¡Si no te detienes, te detendré!"
    pochita "¡Cuidado, Denji!"
    demonio "¡GRRRAAAHHH!"
    power "¡Ataca con cuidado!"
    menu:
        "¿Atacar frontal o esperar estrategia?":
            "Frontal":
                jump rama_3_final_4
            "Esperar":
                jump rama_3_final_2

label rama_4_a:
    scene rooftop_overview
    with fade
    play music "misterio.ogg" fadein 1.0

    "Denji se detiene en el borde del tejado, observando la batalla desde arriba. La lluvia cae sobre su rostro, mezclándose con el sudor y la tensión."
    denji "Tal vez pueda analizarlo primero. No siempre hay que lanzarse de cabeza."
    pochita "¡Denji, vigila todos sus movimientos! Si ves que brilla, ¡corre!"
    aki "Observa sus patrones. Los demonios repiten sus ataques cuando creen que tienen ventaja."
    makima "A veces la paciencia es la mejor arma. El que espera, puede ver lo que otros no ven."
    power "¡Abúrrete menos! ¡Lánzate ya!"
    "Denji observa cómo el demonio ataca a Power y Aki, pero nota que el demonio evita el fuego y los charcos de agua. Makima observa desde otro tejado, como si supiera algo que los demás no."
    menu:
        "¿Qué decides hacer?":
            "Actuar solo y atacar en el momento justo":
                jump rama_4_b
            "Esperar la señal de Makima":
                jump rama_4_makima
            "Unirse a Power y Aki para un ataque coordinado":
                jump rama_4_coordinado
            "Observar más tiempo y buscar debilidades":
                jump rama_4_observar_mas

label rama_4_makima:
    "Denji espera la señal de Makima. Ella levanta la mano y el demonio se detiene, como si sintiera su poder."
    makima "Ahora, Denji."
    denji "¡Voy!"
    "Denji ataca con precisión, guiado por la estrategia de Makima."
    jump rama_4_final_2

label rama_4_coordinado:
    "Denji se une a Power y Aki. Juntos crean una distracción y atacan desde diferentes ángulos."
    power "¡Por el caos!"
    aki "¡Ahora, Denji!"
    "El demonio es derrotado con trabajo en equipo."
    jump rama_2_final_1

label rama_4_observar_mas:
    "Denji observa aún más tiempo y descubre que el demonio tiene miedo a los sonidos agudos."
    pochita "¡Haz ruido, Denji!"
    denji "¡A la motosierra!"
    "El demonio huye, pero deja caer un objeto misterioso: una llave con el símbolo de la División Especial."
    menu:
        "¿Qué haces con la llave?":
            "Investigar su origen":
                jump rama_4_lore
            "Ignorar y atacar":
                jump rama_4_b

label rama_4_lore:
    "Denji investiga la llave y descubre que abre una puerta secreta en la base de la División Especial. Dentro encuentra archivos sobre demonios antiguos y el origen de Pochita."
    pochita "No todo lo que brilla es oro, Denji."
    makima "Algunos secretos deben permanecer ocultos."
    "Denji obtiene información crucial para futuros combates."
    jump rama_4_final_1

# -------------------------
# RAMA 5 – ENFRENTANDO AL DEMONIO NUEVO
# -------------------------
label rama_5_a:
    scene city_ruins_night
    with fade
    play music "danger.ogg" fadein 1.0

    "Un demonio nuevo emerge entre los escombros, con apariencia aterradora y brazos de cadenas. El ambiente está cargado de tensión y misterio, los edificios destruidos cuentan historias de batallas pasadas."
    demonio_nuevo "¡Intrusos! ¡No escaparéis!"
    denji "Esto se ve complicado… ¿Por qué siempre aparecen los raros cuando menos lo espero?"
    pochita "¡Denji, no estamos solos! Este demonio huele diferente, como si guardara un secreto."
    power "¡Aguanta Denji, juntos podemos! Si lo derrotamos, ¡me quedo con sus cadenas!"
    aki "Analiza antes de atacar. Los demonios nuevos suelen tener habilidades ocultas."
    makima "No subestimen lo desconocido. A veces el mayor peligro es lo que no ves."
    "Denji observa que el demonio parece proteger una caja misteriosa entre los escombros."
    menu:
        "¿Qué decides hacer?":
            "Cortar cabeza o cola primero":
                jump rama_5_batalla
            "Investigar la caja antes de atacar":
                jump rama_5_caja
            "Coordinar ataque con Power y Aki":
                jump rama_5_b
            "Esperar a que Makima intervenga":
                jump rama_5_makima

label rama_5_batalla:
    menu:
        "¿Dónde atacas primero?":
            "Cabeza":
                jump rama_5_final_1
            "Cola":
                jump rama_5_final_2

label rama_5_caja:
    "Denji se acerca sigilosamente a la caja. Al abrirla, encuentra un antiguo amuleto con el símbolo de la División Especial y una carta dirigida a él."
    carta "Denji, si lees esto, significa que has superado tus miedos. El verdadero poder está en tu corazón y en tus amigos."
    pochita "¡Eso es muy profundo! ¿Puedo quedarme el amuleto?"
    denji "Tal vez me dé suerte en la pelea."
    "El amuleto brilla y debilita al demonio nuevo, facilitando el combate."
    menu:
        "¿Qué haces ahora?":
            "Atacar con el amuleto":
                jump rama_5_final_1
            "Guardar el amuleto para el futuro":
                jump rama_5_final_5

label rama_5_makima:
    "Makima aparece y usa su poder para debilitar al demonio."
    makima "Denji, termina el trabajo."
    denji "¡Gracias, Makima!"
    "El grupo derrota al demonio y descubre que las cadenas guardan información sobre demonios legendarios."
    menu:
        "¿Qué haces con la información?":
            "Compartir con la División Especial":
                jump rama_5_final_1
            "Guardar el secreto":
                jump rama_5_final_6

# -------------------------
# RAMA 1 – FINALES
# -------------------------
label rama_1_final_1:
    "Final: Denji sobrevive solo, gravemente herido. Aprende la importancia de la estrategia."
    "Denji cae de rodillas, exhausto y herido. La lluvia oculta sus lágrimas mientras recuerda las palabras de Makima y el apoyo de sus amigos."
    pochita "No siempre se gana, Denji. Pero siempre puedes levantarte."
    denji "La próxima vez, pensaré antes de actuar."
    "Denji se recupera lentamente, con nuevas cicatrices y una lección grabada en su corazón."
    return

label rama_1_final_2:
    "Final: Denji y Power sobreviven juntos. Su vínculo se fortalece."
    "Denji y Power se apoyan mutuamente tras la batalla. Power le ofrece su sangre favorita como recompensa."
    power "¡Te lo ganaste, Denji!"
    denji "Gracias, Power. Somos un buen equipo."
    aki "La amistad es la mejor arma."
    pochita "¡Y el pan también!"
    "Ambos prometen protegerse en futuras batallas."
    return

label rama_1_final_3:
    "Final: Demonio escapa parcialmente. Denji aprende que no siempre se gana."
    "El demonio huye entre las sombras, dejando a Denji frustrado pero más sabio."
    denji "No siempre se puede ganar, pero siempre se puede aprender."
    makima "La derrota enseña más que la victoria."
    "Denji observa el horizonte, decidido a mejorar."
    return

label rama_1_final_4:
    "Final: Denji persigue y derrota al demonio, pero con secuelas físicas y emocionales."
    "Denji logra vencer al demonio, pero queda marcado por la batalla. Sus heridas físicas sanan, pero las emocionales tardan más."
    aki "No olvides lo que sentiste hoy, Denji."
    power "¡Las cicatrices son medallas!"
    makima "El dolor es parte del camino."
    "Denji reflexiona sobre el precio de la victoria."
    return

label rama_1_final_5:
    "Final: Refugiarse permite sobrevivir, pero el demonio se fortalece."
    "Denji y el grupo se refugian, evitando el peligro inmediato. Sin embargo, el demonio se fortalece y la amenaza persiste."
    pochita "A veces, sobrevivir es suficiente."
    denji "Pero no podemos huir siempre."
    makima "El enemigo que dejas crecer puede volverse imparable."
    "El grupo se prepara para futuros desafíos."
    return

# -------------------------
# RAMA 2 – FINALES
# -------------------------
label rama_2_final_1:
    "Final: Trabajo en equipo exitoso, demonio derrotado. Denji, Power y Aki consolidan habilidades."
    "El grupo celebra la victoria, compartiendo historias y risas. Denji siente que por fin pertenece a algo más grande que él mismo."
    power "¡Somos los mejores!"
    aki "El trabajo en equipo nos hace invencibles."
    pochita "¡Y el pan nunca falta!"
    makima "La unión es la clave de la fuerza."
    return

label rama_2_final_2:
    "Final: Pelea separada causa bajas menores, pero derrotan al demonio. Cooperación clave."
    "El grupo sufre heridas menores, pero la victoria les enseña la importancia de la cooperación."
    denji "La próxima vez, lucharemos juntos."
    power "¡Menos drama, más acción!"
    aki "La soledad en batalla es peligrosa."
    makima "Aprendan de sus errores."
    return

label rama_2_final_3:
    "Final: Sigilo perfecto, demonio eliminado sin alertar a otros enemigos. Paciencia premiada."
    "Denji y Aki eliminan al demonio con sigilo, evitando una batalla mayor."
    aki "La paciencia es una virtud."
    denji "Nunca subestimes el poder de esperar."
    pochita "¡Menos ruido, más pan!"
    makima "La discreción puede salvar vidas."
    return

label rama_2_final_4:
    "Final: Ataque frontal arriesgado, logran eliminar el demonio con consecuencias graves."
    "El grupo vence al demonio, pero las heridas y el cansancio les recuerdan el precio de la imprudencia."
    denji "A veces, la fuerza no es suficiente."
    power "¡Pero fue épico!"
    aki "La estrategia siempre debe acompañar al valor."
    makima "No olviden lo que han perdido hoy."
    return

# -------------------------
# RAMA 3 – FINALES
# -------------------------
label rama_3_final_1:
    "Final: Denji cumple favor del demonio y gana inesperada alianza."
    "Denji ayuda al demonio, quien le entrega información valiosa y promete ayudar en el futuro."
    demonio "No todos los demonios son enemigos."
    denji "Quizá el mundo no sea tan simple."
    pochita "¡Un aliado inesperado!"
    makima "Las alianzas pueden cambiar el destino."
    return

label rama_3_final_2:
    "Final: Atacar con paciencia, demonio derrotado pero pierde oportunidad de alianza."
    "Denji vence al demonio, pero pierde la oportunidad de obtener información o ayuda."
    denji "A veces, la victoria tiene un precio oculto."
    aki "No subestimes el valor de la palabra."
    makima "La paciencia puede abrir puertas que la violencia cierra."
    return

label rama_3_final_3:
    "Final: Convencer con palabras evita pelea. Denji obtiene información crucial."
    "Denji persuade al demonio y obtiene datos sobre una amenaza mayor."
    demonio "Busca en la División Especial, allí está la clave."
    denji "La información es poder."
    pochita "¡Menos pelea, más pan!"
    makima "La inteligencia puede salvar más que la fuerza."
    return

label rama_3_final_4:
    "Final: Ataca de inmediato y vence, pero pierde posibilidad de alianza."
    "Denji derrota al demonio, pero la oportunidad de una alianza se desvanece."
    denji "No todo se resuelve con violencia."
    power "¡Pero fue divertido!"
    aki "Aprende a elegir tus batallas."
    makima "Las decisiones impulsivas tienen consecuencias."
    return

label rama_4_final_1:
    "Final: Denji vence solo, pero queda herido y aprende paciencia."
    "Denji derrota al demonio, pero las heridas le enseñan el valor de la paciencia y la observación."
    denji "La próxima vez, esperaré el momento justo."
    pochita "¡Eres fuerte, Denji! Pero no olvides pensar."
    makima "La paciencia es la mejor arma."
    return

label rama_4_final_2:
    "Final: Con Makima, victoria estratégica y mínima exposición al peligro."
    "Guiado por Makima, Denji vence al demonio con inteligencia y estrategia."
    makima "La mente es más poderosa que el músculo."
    denji "Gracias, Makima. Aprendí mucho hoy."
    aki "La estrategia nos salva."
    pochita "¡Menos golpes, más pan!"
    return

# -------------------------
# RAMA SECRETA – EL PASADO DE POCHITA
# -------------------------
label rama_secreta_pochita:
    scene pochita_memory
    with fade
    play music "misterio.ogg" fadein 2.0
    "Denji encuentra una puerta secreta en la División Especial y, junto a Pochita, descubre recuerdos del pasado del demonio motosierra."
    pochita "No siempre fui así, Denji. Antes era temido por todos, pero elegí protegerte porque vi algo especial en ti."
    denji "¿Por qué yo?"
    pochita "Porque tienes un corazón que no se rinde."
    menu:
        "¿Qué haces con el secreto?":
            "Compartirlo con el grupo":
                jump final_pochita_grupo
            "Guardarlo solo para ti":
                jump final_pochita_solo

label final_pochita_grupo:
    "El grupo se fortalece al conocer el pasado de Pochita y se preparan para nuevos desafíos."
    makima "El pasado puede doler, pero también puede dar fuerza."
    jump creditos_final

label final_pochita_solo:
    "Denji guarda el secreto, lo que le da una ventaja personal en futuras batallas, pero lo aleja de sus amigos."
    denji "A veces, el poder viene con soledad."
    jump creditos_final

label rama_pan_legendario:
    scene bakery_day
    with fade
    play music "happy.ogg" fadein 1.0
    "Denji, Power y Pochita descubren una panadería secreta en la ciudad. El panero les ofrece el 'Pan Legendario', capaz de curar heridas y dar energía sobrenatural."
    power "¡Quiero diez!"
    pochita "¡Yo veinte!"
    denji "¿Esto es real?"
    panero "Solo para verdaderos héroes."
    menu:
        "¿Qué haces con el pan?":
            "Compartirlo con todos":
                jump final_pan_compartido
            "Guardarlo solo para ti":
                jump final_pan_solo

label final_pan_compartido:
    "El grupo come pan y se siente invencible, listos para enfrentar cualquier demonio. La amistad se fortalece."
    aki "Nunca subestimen el poder del pan."
    makima "Incluso los cazadores necesitan momentos de alegría."
    jump creditos_final

label final_pan_solo:
    "Denji guarda el pan solo para él, obteniendo un poder especial pero generando desconfianza en el grupo."
    denji "El poder tiene un precio."
    jump creditos_final

# -------------------------
# Cambia el inicio del juego para que empiece en introduccion
init python:
    config.start_label = "introduccion"

# -------------------------
# MINI HISTORIA – EL PASADO DE DENJI
# -------------------------
label mini_historia_denji:
    scene denji_past_night
    with fade
    play music "nostalgia.ogg" fadein 2.0
    "La infancia de Denji estuvo marcada por la pobreza extrema. Su padre, endeudado con la yakuza, apenas podía mantenerlo con vida. Cada día era una lucha por conseguir algo de comida, y el miedo a perderlo todo era constante."
    "Denji recuerda noches en las que el hambre le impedía dormir, y días en los que vendía partes de su cuerpo para pagar las deudas heredadas. El dolor físico era nada comparado con la soledad y la desesperanza."
    denji "A veces pensaba que no valía la pena seguir. Pero incluso en los peores momentos, soñaba con una vida normal: una casa, una cama, pan con mermelada y alguien que lo esperara al volver."
    "La yakuza lo utilizaba como herramienta, obligándolo a cazar demonios por dinero. Denji aprendió a sobrevivir en un mundo cruel, donde la compasión era un lujo y la traición, una moneda común."
    "Un día, tras perder a su padre, Denji encontró a Pochita, un demonio motosierra herido. Sin dudarlo, compartió su último trozo de pan con él. Ese acto de bondad fue el inicio de una amistad inquebrantable."
    pochita "Nunca olvidaré ese momento, Denji. Aunque era un demonio, sentí tu dolor y tu esperanza. Por eso decidí quedarme a tu lado."
    "Juntos, enfrentaron la miseria y el peligro. Pochita se convirtió en su única familia, su luz en la oscuridad. Denji aprendió que, aunque el mundo fuera cruel, siempre podía encontrar fuerza en los pequeños gestos de bondad."
    denji "Pochita, tú me diste razones para seguir. Aprendí que el dolor puede ser el motor para cambiar, y que los sueños, aunque pequeños, pueden salvarte."
    "La historia de Denji es una de cicatrices, pero también de esperanza. Cada herida le enseñó a no rendirse, y cada noche oscura le mostró que, incluso en la soledad, puede surgir una nueva oportunidad."
    "Hoy, como Chainsaw Man, Denji lleva consigo el peso de su pasado, pero también la fuerza de quien ha sobrevivido a todo. Su mayor poder no es la motosierra, sino el corazón que nunca se rinde."
    return

