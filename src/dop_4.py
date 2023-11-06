def calculate_area(shape: str, sides: list) -> float | None:
    if shape in ["квадрат", "прямоугольник", "треугольник", "круг"] and sides:
        if shape == "квадрат":
            return sides[0] ** 2
        elif shape == "прямоугольник":
            return sides[0] * sides[1]
        elif shape == "треугольник":
            return 0.5 * sides[0] * sides[1]
        elif shape == "круг":
            return 3.14 * sides[0] ** 2

    else:
        return None
