import streamlit as st
import markdown
from weasyprint import HTML


# Interface para o serviço de Documentação do Sistema
class SystemDocumentationService:
    def generate_documentation(self, readme_file_path):
        markdown_content = self.load_readme_content(readme_file_path)
        html_content = self.convert_to_html(markdown_content)
        pdf_content = self.convert_to_pdf(html_content)
        self.save_pdf_file(pdf_content)

    def load_readme_content(self, readme_file_path):
        with open(readme_file_path, "r") as file:
            content = file.read()
        return content

    def convert_to_html(self, markdown_content):
        return markdown.markdown(markdown_content)

    def convert_to_pdf(self, html_content):
        return HTML(string=html_content).write_pdf()

    def save_pdf_file(self, pdf_content):
        with open("documentation.pdf", "wb") as file:
            file.write(pdf_content)


# Interface para a interface do usuário
class UserInterface:
    def display_generate_documentation_button(self):
        st.title("Sistema de Documentação do Sistema")
        st.markdown("Clique no botão abaixo para gerar a documentação em formato PDF:")

        if st.button("Gerar Documentação"):
            self.generate_documentation()

    def generate_documentation(self):
        documentation_service = SystemDocumentationService()
        readme_file_path = "README.md"
        documentation_service.generate_documentation(readme_file_path)
        st.success("Documentação gerada com sucesso! Clique abaixo para baixar o PDF.")
        self.display_download_link()

    def display_download_link(self):
        with open("documentation.pdf", "rb") as file:
            pdf_data = file.read()
        st.download_button("Baixar Documentação em PDF", pdf_data, file_name="documentation.pdf", mime="application/pdf")


def doc__():
    user_interface = UserInterface()
    user_interface.display_generate_documentation_button()