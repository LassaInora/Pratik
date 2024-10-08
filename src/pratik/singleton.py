class Singleton:
    """A class implementing the Singleton design pattern.

    This class ensures that only one instance of the class exists at any time.
    """

    _instance = None  # The single instance of the class

    def __new__(cls, *args, **kwargs):
        """Creates a new instance of the class, if one does not exist.

        If an instance already exists, it returns the existing instance.
        If arguments are provided and an instance exists, it reinitializes the instance.

        :param args: Positional arguments passed to singleton_init.
        :param kwargs: Keyword arguments passed to singleton_init.
        :return: The single instance of the Singleton class.
        :rtype: Singleton
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.singleton_init(*args, **kwargs)
        elif args or kwargs:
            cls._instance.singleton_init(*args, **kwargs)
        return cls._instance

    def singleton_init(self, *args, **kwargs):
        """Initializes the singleton instance.

        This method is intended to be overridden or extended in subclasses.

        :param args: Positional arguments for initialization.
        :param kwargs: Keyword arguments for initialization.
        """
        pass
