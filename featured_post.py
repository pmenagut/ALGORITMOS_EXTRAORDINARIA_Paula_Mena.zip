# Importar los módulos necesarios para la ejecución del programa.
from datetime import date, datetime
from hashtag import Hashtag
from post import Post

class FeaturedPost(Post):
    """Constructor de la clase.

    El constructor de la clase FeaturedPost se utiliza para crear una nueva publicación destacada.

    Syntax
    ------
      featured_post = FeaturedPost(title, author, pub_date, priority, hashtags)

    Parameters
    ----------
      title : str
        El título de la publicación.
      author : str
        El autor de la publicación.
      pub_date : datetime
        La fecha de publicación de la publicación.
      priority : str
        La prioridad de la publicación destacada (ej. baja, media, alta).
      hashtags : list
        Los hashtags de la publicación.

    Returns
    -------
      La nueva publicación destacada.

    Example
    -------
      featured_post = FeaturedPost("Vacaciones en Bali", "John Doe", datetime(2023, 5, 20), "alta", [Hashtag.TRAVEL, Hashtag.FOOD])
    """

    # Realizar la implementación de la clase FeaturedPost.
    def __init__(self, title, author, date_published, priority, hashtags):
        super().__init__(title, author, date_published, hashtags)
        if priority not in ["baja", "media", "alta"]:
            raise ValueError("Priority must be 'baja', 'media' or 'alta'")
        self.priority = priority

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_date_published(self):
        return self.date_published

    def set_date_published(self, date_published):
        self.date_published = date_published

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def get_hashtags(self):
        return self.hashtags

    def set_hashtags(self, hashtags):
        self.hashtags = hashtags


    def __str__(self):
        hashtags_str = ", ".join([hashtag.value for hashtag in self.hashtags])
        comments_str = ", ".join(self.comments)
        return f"{self.title} de {self.author} con hashtags [{hashtags_str}] y comentarios [{comments_str}] en prioridad {self.priority}."
       

def main():
    """Función principal del módulo.

    La función principal de este módulo se utiliza para probar la Clase FeaturedPost.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a FeaturedPost.")
    print("=================================================================.")
    featured_post = FeaturedPost("Vacaciones en Bali", "John Doe", datetime(2023, 5, 20), "alta", [Hashtag.TRAVEL, Hashtag.FOOD])

    if featured_post.title == "Vacaciones en Bali":
        print("Test PASS. El parámetro title se ha establecido correctamente.")
    else:
        print("Test FAIL. Revisar el método __init__().")

    if featured_post.author == "John Doe":
        print("Test PASS. El parámetro author se ha establecido correctamente.")
    else:
        print("Test FAIL. Revisar el método __init__().")

    if featured_post.date_published == datetime(2023, 5, 20):
        print("Test PASS. El parámetro pub_date se ha establecido correctamente.")
    else:
        print("Test FAIL. Revisar el método __init__().")

    if featured_post.hashtags == [Hashtag.TRAVEL, Hashtag.FOOD]:
        print("Test PASS. El parámetro hashtags se ha establecido correctamente.")
    else:
        print("Test FAIL. Revisar el método __init__().")

    if featured_post.get_priority() == "alta":
        print("Test PASS. El parámetro priority se ha establecido correctamente.")
    else:
        print("Test FAIL. Revisar el método __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class FeaturedPost - String Representation .")
    print("=================================================================.")
    featured_post2 = FeaturedPost("Vacaciones en Bali", "John Doe", datetime(2023, 5, 20), "alta", [Hashtag.TRAVEL.name, Hashtag.FOOD.name])
    featured_post2.add_comment("¡Qué lugar tan hermoso!")
    featured_post2.add_comment("Espero poder ir algún día.")

    expected_str = "Vacaciones en Bali de John Doe con hashtags ['TRAVEL', 'FOOD'] y comentarios ['¡Qué lugar tan hermoso!', 'Espero poder ir algún día.'] en prioridad alta."
    if str(featured_post2) == expected_str:
        print("Test PASS. El formato legible de la publicación destacada se ha implementado correctamente.")
        print(str(featured_post2))
    else:
        print("Test FAIL. Revisar el método __str__()." + " RESULTADO: " + str(featured_post2))

if __name__ == "__main__":
    main()