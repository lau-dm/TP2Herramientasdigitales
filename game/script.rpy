# -------------------------
# DEFINICIÓN DE PERSONAJES CON COLORES
# -------------------------
define d = Character("Denji", color="#FFD700")
define pochita = Character("Pochita", color="#FF8C00")
define p = Character("Power", color="#FF4500")
define a = Character("Aki", color="#1E90FF")
define m = Character("Makima", color="#FF69B4")
define demonio = Character("Demonio", color="#8B0000")
define demonio_nuevo = Character("Demonio Nuevo", color="#880000")

# -------------------------
# INICIO
# -------------------------
label start:
    scene city_rooftop_night
    with fade

    "La ciudad está cubierta de sombras y la lluvia golpea los techos mientras se escuchan gritos de demonios."
    d "Otro día más, otro demonio… ¿por qué siempre yo?"
    pochita "¡Denji, no te preocupes! Yo te respaldo."
    p "¡Vamos, Denji! ¡No te quedes ahí!"
    a "Mantente alerta. No subestimes la situación."
    m "Observa y aprende, Denji. Cada movimiento tiene un precio."

    "De repente, un demonio con brazos como látigos de acero emerge de un callejón."
    demonio "¡Intrusos! ¡Vuestra sangre será mía!"
    d "Maldita sea… ¡Vamos allá!"
    pochita "¡Vamos juntos, Denji!"
    p "¡Cuidado con los brazos!"
    a "Analiza su patrón de ataque."

    menu:
        "¿Qué haces?":
            "Atacar directamente":
                jump rama_1_a
            "Huir y buscar aliados":
                jump rama_2_a
            "Negociar con demonio":
                jump rama_3_a
            "Observar y esperar":
                jump rama_4_a
            "Investigar sonido extraño cercano":
                jump rama_5_a

# -------------------------
# RAMA 1 – ATAQUE DIRECTO
# -------------------------
label rama_1_a:
    scene city_night_rain
    with fade

    d "¡No puedo dejar que lastime a nadie más!"
    p "¡Denji, cuidado! ¡Ese demonio es enorme!"
    a "Nos respaldamos, ve con todo!"
    m "Denji, controla tu fuerza o destruirás todo a tu alrededor."
    pochita "¡Sígueme, Denji! ¡Yo te cubro!"

    "Denji activa la motosierra, cortando el aire con un zumbido metálico."
    "La lluvia intensifica la escena y el reflejo de luces de neón crea destellos sobre charcos de agua."
    "El demonio lanza un golpe, pero Denji logra esquivarlo, dejando marcas profundas en las paredes."

    menu:
        "¿Usas la motosierra completa o parcial?":
            "Completa":
                jump rama_1_b
            "Parcial":
                jump rama_1_c

label rama_1_b:
    "Denji lanza un ataque completo, cortando el aire mientras el demonio retrocede."
    demonio "¡GRRAAAHH!"
    p "¡Cuidado con su cola!"
    a "¡No lo dejes escapar!"
    pochita "¡Estoy contigo, Denji!"

    "De repente, un demonio menor salta desde un edificio cercano."
    demonio "¡Grrr!"
    d "¡Otra vez no!"
    p "¡Denji, tenemos que dividirnos!"
    a "Plan B, rápido."
    pochita "¡Cúbreme mientras atacas!"

    menu:
        "¿Persigues al demonio principal o eliminas al menor primero?":
            "Principal":
                jump rama_1_b_principal
            "Menor":
                jump rama_1_b_menor

label rama_1_b_principal:
    "Denji se concentra en el demonio principal. Power y Aki eliminan al menor."
    d "¡No me detengo hasta que caiga!"
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
    d "¡Maldita sea!"
    p "¡Tenemos que reagruparnos!"
    a "¡Plan B, Denji!"
    pochita "¡Cuidado, Denji!"
    jump rama_1_final_3

label rama_1_c:
    "Herimos parcialmente al demonio, que retrocede entre las sombras."
    d "Volverá más fuerte…"
    p "¡Podemos atraparlo juntos!"
    a "O lo dejamos y planeamos mejor."
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

    "Denji corre por calles oscuras y llenas de escombros."
    p "¡Por aquí, Denji!"
    d "Perfecto, Power. Necesito tu ayuda."
    a "No nos separes. Cada segundo cuenta."
    pochita "¡Denji, confía en mí!"

    menu:
        "¿A quién buscas primero?":
            "Power":
                jump rama_2_b
            "Aki":
                jump rama_2_c

label rama_2_b:
    "Power se une a Denji y ambos planean un ataque estratégico."
    p "¡Denji! Esta vez vamos juntos."
    d "¡Perfecto!"
    a "Si seguimos así, podremos derribarlo rápido."
    pochita "¡Yo cubro la retaguardia!"

    "Una explosión sacude la calle: un demonio bomba aparece."
    demonio "¡Boom!"
    d "¡Cuidado!"
    p "¡Esquiva!"
    a "¡Debemos reagruparnos!"
    pochita "¡Denji, rápido!"

    menu:
        "Cooperar o pelear separados?":
            "Cooperar":
                jump rama_2_final_1
            "Pelea separada":
                jump rama_2_final_2

label rama_2_c:
    "Aki llega y propone un ataque sigiloso."
    a "Debemos mantenernos ocultos y atacar cuando menos lo esperen."
    d "¡Entendido!"
    p "Espero que esto funcione…"
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

    d "Tal vez pueda hablar con él…"
    pochita "¡Denji, sé cuidadoso!"
    p "¿Hablar con un demonio? ¿Estás loco?"
    a "Analiza sus movimientos mientras hablas."
    demonio "¿Hablas o solo vienes a morir?"
    m "Observa y aprende, Denji. Cada palabra importa."

    menu:
        "¿Intentas persuadirlo o amenazarlo?":
            "Persuadir":
                jump rama_3_b
            "Amenazar":
                jump rama_3_c

label rama_3_b:
    d "No necesitamos pelear… podemos llegar a un acuerdo."
    pochita "¡Sí, Denji, mantén la calma!"
    demonio "Hmmm… interesante…"
    a "Sigue con cuidado, Denji."
    menu:
        "¿Ofreces algo a cambio o pides información?":
            "Ofrecer":
                jump rama_3_final_1
            "Pedir información":
                jump rama_3_final_3

label rama_3_c:
    d "¡Si no te detienes, te detendré!"
    pochita "¡Cuidado, Denji!"
    demonio "¡GRRRAAAHHH!"
    p "¡Ataca con cuidado!"
    menu:
        "¿Atacar frontal o esperar estrategia?":
            "Frontal":
                jump rama_3_final_4
            "Esperar":
                jump rama_3_final_2

label rama_4_a:
    scene rooftop_overview
    with fade

    d "Tal vez pueda analizarlo primero."
    pochita "¡Denji, vigila todos sus movimientos!"
    a "Observa sus patrones."
    m "A veces la paciencia es la mejor arma."

    menu:
        "¿Actúas solo o con Makima?":
            "Solo":
                jump rama_4_b
            "Con Makima":
                jump rama_4_c

label rama_4_b:
    "Denji actúa solo, anticipando ataques. Logra vencer al demonio pero queda herido."
    d "Uff… eso estuvo cerca."
    pochita "¡Lo hiciste bien, Denji!"
    jump rama_4_final_1

label rama_4_c:
    "Makima observa y guía a Denji. Vencen al demonio con menos daño y mayor estrategia."
    d "Gracias… Makima."
    m "Siempre observa primero."
    pochita "¡Buen trabajo equipo!"
    jump rama_4_final_2

label rama_5_a:
    scene city_ruins_night
    with fade

    "Un demonio nuevo emerge entre los escombros, con apariencia aterradora y brazos de cadenas."
    demonio_nuevo "¡Intrusos! ¡No escaparéis!"
    d "Esto se ve complicado…"
    pochita "¡Denji, no estamos solos!"
    p "¡Aguanta Denji, juntos podemos!"
    a "Analiza antes de atacar."

    menu:
        "¿Cortar cabeza o cola primero?":
            "Cabeza":
                jump rama_5_final_1
            "Cola":
                jump rama_5_final_2

label rama_5_b:
    menu:
        "¿Coordinar ataque o ir primero?":
            "Coordinación":
                jump rama_5_final_3
            "Tú primero":
                jump rama_5_final_4

label rama_5_c:
    menu:
        "¿Atacar desde lejos o esperar?":
            "Desde lejos":
                jump rama_5_final_5
            "Esperar":
                jump rama_5_final_6

# Rama 1
label rama_1_final_1:
    "Final: Denji sobrevive solo, gravemente herido. Aprende la importancia de la estrategia."
    return

label rama_1_final_2:
    "Final: Denji y Power sobreviven juntos. Su vínculo se fortalece."
    return

label rama_1_final_3:
    "Final: Demonio escapa parcialmente. Denji aprende que no siempre se gana."
    return

label rama_1_final_4:
    "Final: Denji persigue y derrota al demonio, pero con secuelas físicas y emocionales."
    return

label rama_1_final_5:
    "Final: Refugiarse permite sobrevivir, pero el demonio se fortalece."
    return

# Rama 2
label rama_2_final_1:
    "Final: Trabajo en equipo exitoso, demonio derrotado. Denji, Power y Aki consolidan habilidades."
    return

label rama_2_final_2:
    "Final: Pelea separada causa bajas menores, pero derrotan al demonio. Cooperación clave."
    return

label rama_2_final_3:
    "Final: Sigilo perfecto, demonio eliminado sin alertar a otros enemigos. Paciencia premiada."
    return

label rama_2_final_4:
    "Final: Ataque frontal arriesgado, logran eliminar al demonio con consecuencias graves."
    return

# Rama 3
label rama_3_final_1:
    "Final: Denji cumple favor del demonio y gana inesperada alianza."
    return

label rama_3_final_2:
    "Final: Atacar con paciencia, demonio derrotado pero pierde oportunidad de alianza."
    return

label rama_3_final_3:
    "Final: Convencer con palabras evita pelea. Denji obtiene información crucial."
    return

label rama_3_final_4:
    "Final: Ataca de inmediato y vence, pero pierde posibilidad de alianza."
    return

# Rama 4
label rama_4_final_1:
    "Final: Denji vence solo, pero queda herido y aprende paciencia."
    return

label rama_4_final_2:
    "Final: Con Makima, victoria estratégica y mínima exposición al peligro."
    return

# Rama 5
label rama_5_final_1:
    "Final: Nuevo demonio derrotado cortando cabeza. Denji desbloquea arma secreta."
    return

label rama_5_final_2:
    "Final: Nuevo demonio derrotado cortando cola, pero escapa parcialmente."
    return

label rama_5_final_3:
    "Final: Ataque coordinado perfecto, ambos vencen sin daño."
    return

label rama_5_final_4:
    "Final: Denji ataca primero y derrota demonio, Power sufre heridas."
    return

label rama_5_final_5:
    "Final: Atacando desde lejos, Denji observa patrón y lo derrota sin exponerse."
    return

label rama_5_final_6:
    "Final: Esperar demasiado permite que el demonio escape parcialmente."
    return

