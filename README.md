# CICADAS (self-ConstructIng CommutAtive DiAgramS)

Tired of laboriously inputting every coordinate for every node for your commutative diagram? Tired of having to change the whole layout when you decide you want to add something? CICADAS is a command-line tool designed to solve all your commutative diagram typesetting needs!

It offers a unique language designed for describing commutative diagrams at a higher level, automatically plans the diagram and generates a sensible layout for it using simulated annealing. It then outputs the LaTeX representation (using tikz-cd) of that diagram, which you can paste into your existing document.

## Installation

Run `pip install cicadas`

## Usage

Run with:

`cicadas [options] <filename>` (still TODO)

or possibly (depending on installation)

`python main.py [options] <filename>`

```
usage: main.py [-h] [-o O] [-n N] [-p] [--suppress-warnings] file

positional arguments:
  file                 the input file to be parsed

optional arguments:
  -h, --help           show this help message and exit
  -o O                 output destination (will generate a .pdf and a .tex
                       file of that name). Default = './output'
  -n N                 output the best N candidate diagrams. Default = 1
  -p, --preview        automatically open generated pdf in the web browser
                       when finished
  --suppress-warnings  suppresses warnings
```

The layout generation stage uses a random process, so you can expect each run to produce slightly different results (or use the `-n` option to generate a few and pick your favourite one).

The output LaTeX relies on the `tikz-cd` and `amsmath` packages, so be sure to include them in any document you wish to use the output in. Some arrow styles also require the tikz library `decorations.pathmorphing`.

## Language

A CICADAS lanaguage file consists of a sequence of declarations, separated by line breaks and/or semicolons.

### Morphisms

Morphism declarations define which objects and morphisms appear in your diagram. They are declared with the following syntax:

`f: A -> B`

Here `f` is the morphism identifier, while `A` and `B` are object identifiers (higher order morphisms are currently unsupported). These identifiers may be referred to later in further morphism, fact, label or style declarations. Morphism declarations instantiate objects and morphisms, so a morphism defining them must come before any other declaration that uses them.

An identifier may consist of any combination of uppercase letters, lowercase letters and underscores. They may also contain digits, as long as the first character of the identifier is not a digit. Reserved keywords which may not be used as identifiers are `size`, `label`, `style` and `ID`.

If your diagram contains multiple nodes representing the same object (or multiple arrows representing the same morphism), these only need to be declared once. The number of instances of each will be inferred from the declared facts that the diagram should represent.

### Facts

Fact declarations allow you to define how the commutative diagram will be structured, namely which paths in the diagram should be equal.

Paths are dot-separated lists of morphism identifiers (which must already be instantiated) and a fact declaration is a pair of paths, separated by the equals symbol. A possible fact declaration may look like the following:

`g . f = h`

You may also declare that a certain composition of morphisms is the identity (so should yield a loop in the diagram) by using the `ID` keyword, instead of the second path:

`h . g . f = ID`

Equality is symmetric in normal fact declarations (so `f = g` and `g = f` are equivalent), but in identity declarations, the `ID` keyword must come second.

Please note that these declarations are used as heuristics to plan the structure of the commutative diagram, so different sets of facts (which may be mathematically equivalent) may produce different diagrams.

### Labels

Objects and morphisms without explicitly defined labels will by default be labelled with their identifier text in LaTeX inline math mode. If the identifier begins with an underscore, there is no default label.

Labels may be defined with label declarations, such as:

`label T2 : [$T^2$]`

Here T2 is an object or morphism identifier and the text inside the square brackets is the label. This text is passed directly into the LaTeX output, so normal LaTeX restrictions on this apply.

Labels may also be defined inline within morphism declarations:

`f[$f^n$]: X[$X^n$] -> Y[$Y^n$]`

Labels are also supported for regions in the graph, which are implicitly defined by a fact declaration. As these do not have identifiers, these must be specified inline within the fact declaration:

`g . f = h [$h$ def.]`

### Styles

Arrow styles offered by tikz can also be specified. The full list of arrow styles is available in section 1.3 (page 3) of the [tikz-cd manual](http://ctan.math.washington.edu/tex-archive/graphics/pgf/contrib/tikz-cd/tikz-cd-doc.pdf).

A style declaration has the following form:

`style f : (dotted, harpoon)`

Here `f` is a morphism identifier and inside the round brackets is a comma-separated list of all the styles that should be applied to `f`.

Styles may also be defined inline in morphism declarations, which may be combined with inline label definitions:

`f: A -> B (dashed)`

### Size

The dimensions specifying the width and height of the output diagram can be declared with the following:

`size 4.0, 4.0`

Here the first number is the width in centimetres, and the second is the height in centimetres. Other units of measurement are currently unsupported.

### Comments

A comment in this language begins with `//` and ends with the end of the line.

`f: A -> B // this is a comment`

## Example

![Monad diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Coherence_law_for_the_unit_of_a_monad.svg/150px-Coherence_law_for_the_unit_of_a_monad.svg.png)

The commutative diagram representing the identity laws of monads above may be expressed in the CICADAS language with the following:

```
size 4.0, 4.0

_eq          : T -> T (equal)
nT[$\eta T$] : T -> T2[$T^2$]
Tn[$T\eta$]  : T -> T2
mu[$\mu$]    : T2 -> T

mu . Tn = mu . nT
mu . Tn = _eq
mu . nT = _eq
```
