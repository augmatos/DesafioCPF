from validadorCPF import valida_cpf
from geradorCPF import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor
import design
import sys


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    """Aplicação GUI para validar e gerar CPFs."""

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # Conecta os botões às funções
        self.btnGeraCPF.clicked.connect(self.gerar_cpf)
        self.btnValidaCPF.clicked.connect(self.validar_cpf)

    def gerar_cpf(self) -> None:
        """Gera um CPF válido e exibe na interface."""
        try:
            cpf_gerado = gera_cpf(formatado=True)
            self._mostrar_sucesso(f"CPF Gerado: {cpf_gerado}")
            self.inputValidaCPF.setText(cpf_gerado)
        except Exception as e:
            self._mostrar_erro(f"Erro ao gerar CPF: {str(e)}")

    def validar_cpf(self) -> None:
        """Valida o CPF fornecido no campo de entrada."""
        try:
            cpf = self.inputValidaCPF.text().strip()

            if not cpf:
                self._mostrar_erro("Por favor, insira um CPF")
                return

            if valida_cpf(cpf):
                self._mostrar_sucesso("✓ CPF VÁLIDO")
            else:
                self._mostrar_erro("✗ CPF INVÁLIDO")

        except Exception as e:
            self._mostrar_erro(f"Erro: {str(e)}")

    def _mostrar_sucesso(self, mensagem: str) -> None:
        """Exibe mensagem de sucesso com cor verde."""
        self.labelRetorno.setText(mensagem)
        self.labelRetorno.setStyleSheet("color: green; font-weight: bold;")

    def _mostrar_erro(self, mensagem: str) -> None:
        """Exibe mensagem de erro com cor vermelha."""
        self.labelRetorno.setText(mensagem)
        self.labelRetorno.setStyleSheet("color: red; font-weight: bold;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = GeraValidaCPF()
    janela.show()
    sys.exit(app.exec_())
