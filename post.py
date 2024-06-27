# Importar los módulos necesarios para la ejecución del programa.
from datetime import date, datetime
from hashtag import Hashtag

class Post:
    """Constructor for the Post class.

    The constructor for the Post class is used to create a new post.

    Syntax
    ------
        post = Post(title, author, date_published, hashtags)
    
    Parameters
    ----------
    title : str
        The title of the post.
    author : str
        The author of the post.
    date_published : datetime
        The date the post was published.
    hashtags : set, optional
        A set of hashtags associated with the post.
    
    Returns
    -------
        The new post.

    Example
    -------
        post = Post("Vacaciones en Bali", "John Doe", datetime.now(), [Hashtag.TRAVEL])
    """
    #Realizar la implementación de la clase Post.
    def __init__(self, title, author, date_published, hashtags):
        if not isinstance(title, str):
            raise ValueError("Tittle must be a string")
        if not isinstance(author, str):
            raise ValueError("Author must be a string")
        if not isinstance(date_published, date):
            raise ValueError("Publication date must be a valid date and not a future date")
        
        self.title = title
        self.author = author
        self.date_published = date_published
        self.hashtags = set()
        if hashtags:
            for hashtag in hashtags:
                self.add_hashtag(hashtag)
        self.comments = []


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

    def get_hashtags(self):
        return self.hashtags

    def set_hashtags(self, hashtags):
        self.hashtags = hashtags

    



    def add_hashtag(self, hashtag):
        """Adds a hashtag to the post if not already present."""
        if isinstance(hashtag, Hashtag):
            self.hashtags.add(hashtag)
        pass
    
    def add_comment(self, comment):
        """Adds a comment to the post."""
        if not isinstance(comment, str):
            raise ValueError("Comment must be a string")
        self.comments.append(comment)
        pass

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return self.title == other.title and self.author == other.author and self.date_published == other.date_published
    
    def __str__(self):
        hashtags_str = ", ".join([hashtag.value for hashtag in self.hashtags])
        comments_str = ", ".join(self.comments)
        return f"{self.title} de {self.author} con hashtags [{hashtags_str}] y comentarios [{comments_str}]"

def main():
    """Function main of the module to test the Class Post."""
    print("=================================================================.")
    print("Test Case 1: Check Class Post - Initialization.")
    print("=================================================================.")
    
    date_published = datetime.now()
    hashtags = {Hashtag.TRAVEL, Hashtag.FOOD}
    
    try:
        post = Post("Vacaciones en Bali", "John Doe", date_published, hashtags)
        print("Test PASS. The Post has been correctly initialized.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 2: Check Class Post - Add Hashtag.")
    print("=================================================================.")
    
    try:
        post.add_hashtag(Hashtag.FASHION)
        if Hashtag.FASHION in post.hashtags:
            print("Test PASS. The Hashtag has been correctly added.")
        else:
            print("Test FAIL. The Hashtag has not been added.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 3: Check Class Post - Add Comment.")
    print("=================================================================.")
    
    try:
        post.add_comment("¡Qué hermoso lugar!")
        if "¡Qué hermoso lugar!" in post.comments:
            print("Test PASS. The Comment has been correctly added.")
        else:
            print("Test FAIL. The Comment has not been added.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 4: Check Class Post - Equality.")
    print("=================================================================.")
    
    try:
        another_post = Post("Vacaciones en Bali", "John Doe", date_published, hashtags)
        if post == another_post:
            print("Test PASS. The equality method works correctly.")
        else:
            print("Test FAIL. The equality method does not work correctly.")
    except Exception as e:
        print(f"Test FAIL. {e}")
    
    print("=================================================================.")
    print("Test Case 5: Check Class Post - String Representation.")
    print("=================================================================.")
    post2 = Post("Vacaciones en Bali", "John Doe", datetime(2023, 5, 20), [Hashtag.TRAVEL.name, Hashtag.FOOD.name])
    post2.add_comment("¡Qué lugar tan hermoso!")
    post2.add_comment("Espero poder ir algún día.")

    expected_str = "Vacaciones en Bali de John Doe con hashtags ['TRAVEL', 'FOOD'] y comentarios ['¡Qué lugar tan hermoso!', 'Espero poder ir algún día.']."
    if str(post2) == expected_str:
        print("Test PASS. El formato legible de la publicación destacada se ha implementado correctamente.")
        print(str(post2))
    else:
        print("Test FAIL. Revisar el método __str__()." + " RESULTADO: " + str(post2))

if __name__ == "__main__":
    main()