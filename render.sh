if [ "$1" = "--high-quality" ]; then 
    manim main.py RubiksCubeScene -p
else 
    manim main.py RubiksCubeScene -pl
fi
