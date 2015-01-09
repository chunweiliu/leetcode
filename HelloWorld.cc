#include <iostream>

class HelloWorld
{
public:
	HelloWorld();
	~HelloWorld();	
};

HelloWorld::HelloWorld()
{
	std::cout << "Hello World!" << std::endl;
}

HelloWorld::~HelloWorld()
{

}

int main()
{
	HelloWorld hello_world;
}