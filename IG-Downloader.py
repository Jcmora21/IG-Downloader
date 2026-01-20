import instaloader
import sys

def download_profile(username):
    L = instaloader.Instaloader(
        download_pictures=True,     # Baixa fotos
        download_videos=True,       # Baixa vídeos
        download_comments=False,    # Comente se quiser comentários (mais lento)
        download_geotags=True,      # Geotags
        download_stories=True,      # Stories (se disponíveis)
        save_metadata=True          # Salva JSON com metadata
    )

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        L.download_profile(profile, profile_pic=True)  # Baixa perfil inteiro
        print(f"\nPerfil '{username}' baixado com sucesso na pasta atual!")
    except Exception as e:
        print(f"Erro: {e}. Verifique se o perfil existe ou é público.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1].lstrip('@')  # Remove @ se tiver
    else:
        username = input("Digite o @username (ex: @exemplo): ").lstrip('@')
    
    download_profile(username)
