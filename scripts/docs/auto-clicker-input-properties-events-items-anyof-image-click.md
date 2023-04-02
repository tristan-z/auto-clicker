# Image Click Schema

```txt
auto-clicker-input.schema.json#/properties/children/items/anyOf/3
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                          |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [auto-clicker-input.schema.json\*](../../out/auto-clicker-input.schema.json "open original schema") |

## 3 Type

`object` ([Image Click](auto-clicker-input-properties-events-items-anyof-image-click.md))

# 3 Properties

| Property                               | Type          | Required | Nullable       | Defined by                                                                                                                                                                                                        |
| :------------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [notes](#notes)                        | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/notes")                       |
| [type](#type)                          | Not specified | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/type")                         |
| [click\_type](#click_type)             | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-click_type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/click_type")             |
| [pixel\_offset](#pixel_offset)         | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-pixel_offset.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/pixel_offset")         |
| [image\_path](#image_path)             | `string`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-image_path.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/image_path")             |
| [confidence](#confidence)              | `number`      | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-confidence.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/confidence")             |
| [grayscale](#grayscale)                | `boolean`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-grayscale.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/grayscale")               |
| [region](#region)                      | `array`       | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-region.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/region")                                                                     |
| [attempts](#attempts)                  | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-attempts.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/attempts")                 |
| [execution\_modulo](#execution_modulo) | `integer`     | Optional | cannot be null | [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/execution_modulo") |
| [iterations](#iterations)              | `object`      | Required | cannot be null | [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/iterations")                                                             |

## notes



`notes`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-notes.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/notes")

### notes Type

`string`

## type



`type`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/type")

### type Type

unknown

### type Constraints

**constant**: the value of this property must be equal to:

```json
"IMAGE_CLICK"
```

## click\_type



`click_type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-click_type.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/click_type")

### click\_type Type

`string`

### click\_type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"left"`  |             |
| `"right"` |             |

## pixel\_offset



`pixel_offset`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-pixel_offset.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/pixel_offset")

### pixel\_offset Type

`integer`

## image\_path



`image_path`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-image_path.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/image_path")

### image\_path Type

`string`

## confidence



`confidence`

*   is optional

*   Type: `number`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-confidence.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/confidence")

### confidence Type

`number`

## grayscale



`grayscale`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-grayscale.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/grayscale")

### grayscale Type

`boolean`

## region



`region`

*   is optional

*   Type: `array` ([region](auto-clicker-input-defs-region.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-region.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/region")

### region Type

`array` ([region](auto-clicker-input-defs-region.md))

## attempts



`attempts`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-attempts.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/attempts")

### attempts Type

`integer`

## execution\_modulo



`execution_modulo`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-properties-events-items-anyof-image-click-properties-execution_modulo.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/execution_modulo")

### execution\_modulo Type

`integer`

## iterations



`iterations`

*   is required

*   Type: `object` ([iterations](auto-clicker-input-defs-iterations.md))

*   cannot be null

*   defined in: [Auto Clicker Input](auto-clicker-input-defs-iterations.md "auto-clicker-input.schema.json#/properties/children/items/anyOf/3/properties/iterations")

### iterations Type

`object` ([iterations](auto-clicker-input-defs-iterations.md))
