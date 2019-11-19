# Part II Project (package name TBC)

Using Python 3.7.8

## Language Spec (WIP)

### Possible expressions

- A morphism: `f: C1 -> C2`
- A fact: `f . g = h . k` (two arbitrary paths either side of the equals sign)
  - *is this too forgiving syntax?*
- A label: `label identifier = label_text` (if unspecified, the object/functor identifier is used as the label text)
- Second order maps: `f: g -> h`
Introduce a type system to allow only second order maps (bonus points in the diss)? So by default, this syntax will assume the two targets to be categories, but if they've previously been defined as first order maps, it will become a second order map.
