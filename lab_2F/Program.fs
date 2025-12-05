open System

type GeometricFigure =
    | Rectangle of width: float * height: float
    | Square of side: float
    | Circle of radius: float


let S figure =
    match figure with
    | Rectangle(w, h) -> w * h
    | Square(s) -> s * s
    | Circle(r) -> Math.PI * r * r

let printFigure figure =
    let area = S figure
    match figure with
    | Rectangle(w, h) -> 
        printfn "Прямоугольник: ширина = %.2f, высота = %.2f, площадь = %.2f" w h area
    | Square(s) -> 
        printfn "Квадрат: сторона = %.2f, площадь = %.2f" s area
    | Circle(r) -> 
        printfn "Круг: радиус = %.2f, площадь = %.2f" r area

[<EntryPoint>]
let main argv =
    let rect = Rectangle(5.0, 3.0)
    let square = Square(4.0)
    let circle = Circle(2.0)

    printFigure rect
    printFigure square
    printFigure circle

    0
