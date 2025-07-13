import praw
import time

# Configura tu acceso a Reddit
reddit = praw.Reddit(
    client_id="zkxwr4VILBRrbdvsNwdlQw",
    client_secret="ENOBBG7YyoXN7DkFkcE1E6i7eLMLfA",
    username="MuchPercentage7528",
    password="AJGG123aj",
    user_agent="script:MiBotTrabajo:v1.0 (by u/MuchPercentage7528)"
)

# Subreddit donde buscar
subreddit = reddit.subreddit("forhire")

print("🤖 Bot de ofertas de trabajo iniciado...\n")

# Bucle infinito que se ejecuta cada 15 minutos
while True:
    print("🔄 Buscando publicaciones con 'hiring' en el título...\n")

    for post in subreddit.new(limit=50):
        title = post.title.lower()
        if "hiring" in title:
            print("🔔 Oferta encontrada:")
            print(f"Título: {post.title}")
            print(f"Enlace: {post.url}")
            print("---")

    print("😴 Esperando 15 minutos...\n")
    time.sleep(900)  # 900 segundos = 15 minutos

