import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):

    def __init__(self):
        super().__init__()

        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):

        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)

        elif tag == "input":
            self.inputs.append(attrs)

        elif tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        html_file = Path(__file__).parent / "index.html"

        if not html_file.exists():
            raise FileNotFoundError(
                "index.html file not found!"
            )

        html_content = html_file.read_text(
            encoding="utf-8"
        )

        cls.parser = FormParser()
        cls.parser.feed(html_content)

    def test_form_exists(self):

        self.assertGreater(
            len(self.parser.forms),
            0,
            "HTML form is missing!"
        )

    def test_name_field_exists(self):

        name_fields = [
            field for field in self.parser.inputs
            if field.get("name") == "name"
        ]

        self.assertTrue(
            name_fields,
            "Name field is missing!"
        )

        self.assertEqual(
            name_fields[0].get("type"),
            "text",
            "Name field must be of type text!"
        )

    def test_email_field_exists(self):

        email_fields = [
            field for field in self.parser.inputs
            if field.get("name") == "email"
        ]

        self.assertTrue(
            email_fields,
            "Email field is missing!"
        )

        self.assertEqual(
            email_fields[0].get("type"),
            "email",
            "Email field must be of type email!"
        )

    def test_contact_field_exists(self):

        contact_fields = [
            field for field in self.parser.inputs
            if field.get("name") == "contact"
        ]

        self.assertTrue(
            contact_fields,
            "Contact Number field is missing!"
        )

        self.assertEqual(
            contact_fields[0].get("type"),
            "tel",
            "Contact field must be of type tel!"
        )

    def test_submit_button_exists(self):

        submit_buttons = [
            button for button in self.parser.buttons
            if button.get("type") == "submit"
        ]

        self.assertTrue(
            submit_buttons,
            "Submit button is missing!"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)