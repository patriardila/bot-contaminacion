import discord
from discord.ext import commands
import requests
intents= discord.Intents.default()
intents.message_content=True

bot=commands.Bot(command_prefix="/",intents=intents)

UNSPLASH_ACCESS_KEY = ''#AQUI DBE IR LA CLAVE DE ACCESO A LA API DE UNPLASH

@bot.event
async def on_reday():
    print(f"hemos iniciado sesion {bot.user}")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_contamination_image():
    query = "contaminación"
    url = f"https://api.unsplash.com/photos/random?query={query}&client_id={UNSPLASH_ACCESS_KEY}" #Crea la URL de la API de Unsplash, utilizando una f-string para incluir la variable query y la clave de acceso UNSPLASH_ACCESS_KEY. La URL solicita una imagen aleatoria relacionada con la contaminación desde Unsplash.
    response = requests.get(url) #Realiza una solicitud HTTP GET a la URL definida. Se utiliza la biblioteca requests para obtener datos desde la API de Unsplash.
    data = response.json()
    return data['urls']


@bot.command()
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

descomposicion={
    "botella":500,
    "lata":50,
    "bolsa":150,
    "vidrio":4000
}

@bot.command()
async def impacto(ctx,objeto):
    objeto=objeto.lower()
    if objeto in descomposicion:
        tiempo=descomposicion[objeto]
        await ctx.send(f"El objeto{objeto},dura aprox {tiempo} en descomponerse")
        if tiempo>=100:
            await ctx.send(f"S.O.S nos quedamos sin planeta")
    else: 
        await ctx.send("No registro ese objeto")

recycling_ideas = {
    "plástico": ["macetas para plantas", "joyería artesanal", "ladrillos ecológicos"],
    "papel": ["cuadernos reciclados", "decoraciones para el hogar", "papel maché"],
    "vidrio": ["lámparas decorativas", "jarrones", "ladrillos de vidrio"],
    "metal": ["macetas", "arte decorativo", "portavelas"],
    "cartón": ["organizadores de escritorio", "casitas para mascotas", "manualidades infantiles"],
}
@bot.command()
async def reciclar(ctx, elemento: str):
    elemento = elemento.lower()  # Convertir a minúsculas para evitar errores de entrada
    if elemento in recycling_ideas:
        objetos =recycling_ideas[elemento]
        await ctx.send(f"Con {elemento} puedes hacer: {objetos}.")
    else:
        await ctx.send("Lo siento, no tengo ideas de reciclaje para ese elemento.")


@bot.command()
async def contam(ctx):
    image_url = get_contamination_image()
    if image_url:
        await ctx.send(f"Aquí tienes una imagen sobre contaminación: {image_url}")
    else:
        await ctx.send('No pude obtener la imagen. Por favor, intenta más tarde.')
   

bot.run("") #AQUI DEBE IR EL TOKEN DE SU BOT



