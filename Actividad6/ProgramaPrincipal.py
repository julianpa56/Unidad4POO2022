
# PROGRAMA PRINCIPAL
from claseRepositorioProvincia import RespositorioProvincias
from Clases import VistaProvincia
from claseControladorProvincia import ControladorProvincias
from claseObjectEncoder import ObjectEncoder


def main():
    conn=ObjectEncoder('provincias.json')
    repo=RespositorioProvincias(conn)
    vista=VistaProvincia()
    ctrl=ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()


if __name__ == "__main__":
    main()