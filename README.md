# CICADAS (self-ConstructIng CommutAtive DiAgramS)

## Installation

Run `pip install cicadas`

## Usage

Run with:

`cicadas [options] <filename>`

or possibly (depending on installation)

`python main.py [options] <filename>`

### Options

```shell
usage: main.py [-h] [-o O] [-n N] [-q QUALITY] [-p] [-c] [--suppress-warnings]
               filename

CICADAS description

positional arguments:
  filename              the input file to be parsed

optional arguments:
  -h, --help            show this help message and exit
  -o O                  output destination (will generate a .pdf and a .tex
                        file of that name). Default: './output'
  -n N                  number of candidate diagrams to generate
  -q QUALITY, --quality QUALITY
                        adjust running time to affect quality. acceptable are
                        integers > 0. default = 5
  -p, --preview         automatically open generated pdf when finished
  -c, --auto-clipboard  automatically copy tikz output to clipboard
  --suppress-warnings   suppresses warnings
```

## Language

A CICADAS lanaguage file consists of a sequence of declarations, separated by line breaks and/or semicolons.

### Arrows

Arrow declarations define which nodes and arrows appear in your diagram. They are declared with the following syntax:

`f: A -> B`

Here `f` is the arrow identifier, while `A` and `B` are node identifiers (higher order morphisms are currently unsupported). These identifiers may be referred to later in further arrow, fact, label or style declarations. Arrow declarations instantiate nodes and edges, so an arrow defining them must come before any other declaration that uses them.

An identifier may consist of any combination of uppercase letters, lowercase letters and underscores. They may also contain digits, as long as the first character of the identifier is not a digit. Reserved keywords which may not be used as identifiers are `size`, `label`, `style` and `ID`.

If your diagram contains multiple instances of particular nodes or arrows, these only need to be declared once. The number of instances of each will be inferred from the declared facts that the diagram should represent.

### Facts

Fact declarations allow you to define how the commutative diagram will be structured, namely which paths in the diagram should be equal.

Paths are dot-separated lists of arrow identifiers (which must already be instantiated) and a fact declaration is a pair of paths, separated by the equals symbol. A possible fact declaration may look like the following:

`g . f = h`

You may also declare that a certain composition of arrows is the identity (so should yield a loop in the diagram) by using the `ID` keyword, instead of the second path:

`h . g . f = ID`

Equality is symmetric in normal fact declarations (so `f = g` and `g = f` are equivalent), but in identity declarations, the `ID` keyword must come second.

Please note that these declarations are used as heuristics to plan the structure of the commutative diagram, so different sets of facts (which may be mathematically equivalent) may produce different diagrams.

### Labels

Nodes and arrows without explicitly defined labels will by default be labelled with their identifier text in inline math mode. If the identifier begins with an underscore, there is no default label.

Labels may be defined with label declarations, such as:

`label T2 : [$T^2$]`

Here T2 is a node or arrow identifier and the text inside the square brackets is the label. This text is passed directly into the LaTeX output, so normal LaTeX restrictions on this apply.

Labels may also be defined inline within arrow declarations:

`f[$f^n$]: X[$X^n$] -> Y[$Y^n$]`

Labels are also supported for regions in the graph, which are implicitly defined by a fact declaration. As these do not have identifiers, these must be specified inline within the fact declaration:

`g . f = h [$h$ def.]`

### Styles

Arrow styles offered by tikz can also be specified. The full list of arrow styles is available in section 1.3 (page 3) of the [tikz-cd manual](http://ctan.math.washington.edu/tex-archive/graphics/pgf/contrib/tikz-cd/tikz-cd-doc.pdf).

A style declaration has the following form:

`style f : (dotted, harpoon)`

Here `f` is an arrow identifier and inside the round brackets is a comma-separated list of all the styles that should be applied to `f`.

Styles may also be defined inline in arrow declarations, which may be combined with inline label definitions:

`f: A -> B (dashed)`

### Size

The dimensions specifying the width and height of the output diagram can be declared with the following:

`size 4.0, 4.0`

Here the first number is the width in centimetres, and the second is the height in centimetres. Other units of measurement are currently unsupported.

## Example

![Monad diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Coherence_law_for_the_unit_of_a_monad.svg/150px-Coherence_law_for_the_unit_of_a_monad.svg.png)

The commutative diagram representing the monad category above may be expressed in the CICADAS language with the following:

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
