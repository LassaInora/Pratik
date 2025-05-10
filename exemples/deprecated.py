from pratik import deprecated

@deprecated
class DeprecatedClass:
    pass

@deprecated("Use OtherClass() instead.")
class OtherDeprecatedClass:
    pass

@deprecated
def deprecated_function():
    pass

@deprecated("Use other_function() instead.")
def other_deprecated_function():
    pass

if __name__ == "__main__":
    var1 = DeprecatedClass()
    var2 = OtherDeprecatedClass()
    deprecated_function()
    other_deprecated_function()
