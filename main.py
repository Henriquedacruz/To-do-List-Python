from interface_tk import App
from banco import inicializar_db

def main():
    inicializar_db()
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
