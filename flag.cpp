#include <SFML/Graphics.hpp>
using namespace sf; 
int main() {
    // Create a window
    RenderWindow window(VideoMode(600, 400), "Bangladesh Flag");

    // Create green rectangle (flag background)
    RectangleShape flag(Vector2f(300.f, 180.f));
    flag.setFillColor(Color(0, 106, 78)); // Official green
    flag.setPosition(150.f, 110.f); // Centered

    // Create red circle
    CircleShape circle(60.f);
    circle.setFillColor(Color(244, 42, 65)); // Official red
    circle.setPosition(150.f + 60.f, 110.f + 30.f); // Slightly to left

    while (window.isOpen()) {
        Event event;
        while (window.pollEvent(event)) {
            if (event.type == Event::Closed)
                window.close();
        }

        window.clear(Color::White);
        window.draw(flag);
        window.draw(circle);
        window.display();
    }

    return 0;
}

// To run the code use the following commands in terminal
// g++ flag.cpp -o flag -lsfml-graphics -lsfml-window -lsfml-system
// ./flag