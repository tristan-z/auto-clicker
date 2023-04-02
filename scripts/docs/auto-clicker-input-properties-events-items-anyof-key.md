# Key Schema

```txt
auto-clicker-input.schema.json#/properties/children/items/anyOf/2
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [auto-clicker-input.schema.json\*](../../out/auto-clicker-input.schema.json "open original schema") |

## 2 Type

`object` ([Key](auto-clicker-input-properties-events-items-anyof-key.md))

# 2 Properties

| Property                               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                |
| :------------------------------------- | :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [notes](#notes)                        | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/notes")                       |
| [type](#type)                          | Not specified | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/type")                         |
| [click\_type](#click_type)             | Not specified | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-click_type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/click_type")             |
| [key](#key)                            | Not specified | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-key.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/key")                           |
| [execution\_modulo](#execution_modulo) | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/execution_modulo") |
| [iterations](#iterations)              | `object`      | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/iterations")                                                     |

## notes



`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/notes")

### notes Type

`string`

## type



`type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/type")

### type Type

unknown

### type Constraints

**constant**: the value of this property must be equal to:

```json
"KEY"
```

## click\_type



`click_type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-click_type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/click_type")

### click\_type Type

unknown

### click\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"press"`   |             |
| `"release"` |             |
| `"hold"`    |             |

## key



`key`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-key.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/key")

### key Type

unknown

### key Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | :---------- |
| `"\t"`                |             |
| `"\n"`                |             |
| `"\r"`                |             |
| `" "`                 |             |
| `"!"`                 |             |
| `"\""`                |             |
| `"#"`                 |             |
| `"$"`                 |             |
| `"%"`                 |             |
| `"&"`                 |             |
| `"'"`                 |             |
| `"("`                 |             |
| `")"`                 |             |
| `"*"`                 |             |
| `"+"`                 |             |
| `","`                 |             |
| `"-"`                 |             |
| `"."`                 |             |
| `"/"`                 |             |
| `"0"`                 |             |
| `"1"`                 |             |
| `"2"`                 |             |
| `"3"`                 |             |
| `"4"`                 |             |
| `"5"`                 |             |
| `"6"`                 |             |
| `"7"`                 |             |
| `"8"`                 |             |
| `"9"`                 |             |
| `":"`                 |             |
| `";"`                 |             |
| `"<"`                 |             |
| `"="`                 |             |
| `">"`                 |             |
| `"?"`                 |             |
| `"@"`                 |             |
| `"["`                 |             |
| `"\\"`                |             |
| `"]"`                 |             |
| `"^"`                 |             |
| `"_"`                 |             |
| ``"`"``               |             |
| `"a"`                 |             |
| `"b"`                 |             |
| `"c"`                 |             |
| `"d"`                 |             |
| `"e"`                 |             |
| `"f"`                 |             |
| `"g"`                 |             |
| `"h"`                 |             |
| `"i"`                 |             |
| `"j"`                 |             |
| `"k"`                 |             |
| `"l"`                 |             |
| `"m"`                 |             |
| `"n"`                 |             |
| `"o"`                 |             |
| `"p"`                 |             |
| `"q"`                 |             |
| `"r"`                 |             |
| `"s"`                 |             |
| `"t"`                 |             |
| `"u"`                 |             |
| `"v"`                 |             |
| `"w"`                 |             |
| `"x"`                 |             |
| `"y"`                 |             |
| `"z"`                 |             |
| `"{"`                 |             |
| `"\|"`                |             |
| `"}"`                 |             |
| `"~"`                 |             |
| `"accept"`            |             |
| `"add"`               |             |
| `"alt"`               |             |
| `"altleft"`           |             |
| `"altright"`          |             |
| `"apps"`              |             |
| `"backspace"`         |             |
| `"browserback"`       |             |
| `"browserfavorites"`  |             |
| `"browserforward"`    |             |
| `"browserhome"`       |             |
| `"browserrefresh"`    |             |
| `"browsersearch"`     |             |
| `"browserstop"`       |             |
| `"capslock"`          |             |
| `"clear"`             |             |
| `"convert"`           |             |
| `"ctrl"`              |             |
| `"ctrlleft"`          |             |
| `"ctrlright"`         |             |
| `"decimal"`           |             |
| `"del"`               |             |
| `"delete"`            |             |
| `"divide"`            |             |
| `"down"`              |             |
| `"end"`               |             |
| `"enter"`             |             |
| `"esc"`               |             |
| `"escape"`            |             |
| `"execute"`           |             |
| `"f1"`                |             |
| `"f10"`               |             |
| `"f11"`               |             |
| `"f12"`               |             |
| `"f13"`               |             |
| `"f14"`               |             |
| `"f15"`               |             |
| `"f16"`               |             |
| `"f17"`               |             |
| `"f18"`               |             |
| `"f19"`               |             |
| `"f2"`                |             |
| `"f20"`               |             |
| `"f21"`               |             |
| `"f22"`               |             |
| `"f23"`               |             |
| `"f24"`               |             |
| `"f3"`                |             |
| `"f4"`                |             |
| `"f5"`                |             |
| `"f6"`                |             |
| `"f7"`                |             |
| `"f8"`                |             |
| `"f9"`                |             |
| `"final"`             |             |
| `"fn"`                |             |
| `"hanguel"`           |             |
| `"hangul"`            |             |
| `"hanja"`             |             |
| `"help"`              |             |
| `"home"`              |             |
| `"insert"`            |             |
| `"junja"`             |             |
| `"kana"`              |             |
| `"kanji"`             |             |
| `"launchapp1"`        |             |
| `"launchapp2"`        |             |
| `"launchmail"`        |             |
| `"launchmediaselect"` |             |
| `"left"`              |             |
| `"modechange"`        |             |
| `"multiply"`          |             |
| `"nexttrack"`         |             |
| `"nonconvert"`        |             |
| `"num0"`              |             |
| `"num1"`              |             |
| `"num2"`              |             |
| `"num3"`              |             |
| `"num4"`              |             |
| `"num5"`              |             |
| `"num6"`              |             |
| `"num7"`              |             |
| `"num8"`              |             |
| `"num9"`              |             |
| `"numlock"`           |             |
| `"pagedown"`          |             |
| `"pageup"`            |             |
| `"pause"`             |             |
| `"pgdn"`              |             |
| `"pgup"`              |             |
| `"playpause"`         |             |
| `"prevtrack"`         |             |
| `"print"`             |             |
| `"printscreen"`       |             |
| `"prntscrn"`          |             |
| `"prtsc"`             |             |
| `"prtscr"`            |             |
| `"return"`            |             |
| `"right"`             |             |
| `"scrolllock"`        |             |
| `"select"`            |             |
| `"separator"`         |             |
| `"shift"`             |             |
| `"shiftleft"`         |             |
| `"shiftright"`        |             |
| `"sleep"`             |             |
| `"space"`             |             |
| `"stop"`              |             |
| `"subtract"`          |             |
| `"tab"`               |             |
| `"up"`                |             |
| `"volumedown"`        |             |
| `"volumemute"`        |             |
| `"volumeup"`          |             |
| `"win"`               |             |
| `"winleft"`           |             |
| `"winright"`          |             |
| `"yen"`               |             |
| `"command"`           |             |
| `"option"`            |             |
| `"optionleft"`        |             |
| `"optionright"`       |             |

## execution\_modulo



`execution_modulo`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-key-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/execution_modulo")

### execution\_modulo Type

`integer`

## iterations



`iterations`

*   is required

*   Type: `object` ([iterations](auto-clicker-input-defs-iterations.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/2/properties/iterations")

### iterations Type

`object` ([iterations](auto-clicker-input-defs-iterations.md))
