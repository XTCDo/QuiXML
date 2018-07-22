# quixml
Easy xml formatting

## How to use
Run the `quixml.py` file inside any folder with `.txt` files. QuiXML will create formatted `.xml` files out of the `.txt` files.

QuiXML will overwrite any created `.xml` file when it detects a change in it's original `.txt` file.

**Make sure that you use a completely separate folder for QuiXML usage, you might accidentally overwrite other important `.xml` files!`**
## Tags
### Regular tags
Type the name of your tags and indent them with spaces if they should be nested inside another tag

**Example**

Input:
```
first-tag
second-tag
 nested-tag
```
Output:

```xml
<first-tag>
</first-tag>
<second-tag>
 <nested-tag>
 </nested-tag>
</second-tag>
```

### Tags with content
Most tags, like `<h1>Title</h1>` in html for example have text inbetween the opening and closing tag

**Example**

Input:
```
first-tag text inside the tag
second-tag
 nested-tag text inside nested tag
```
Output:

```xml
<first-tag>
 text inside the tag
</first-tag>
<second-tag>
 <nested-tag>
  text inside the nested tag
 </nested-tag>
</second-tag>
```

### Tags with attributes
Sometimes tags have attributes like `<h1 class="title">Title page</h1>`

**Example**

Input:
```
first-tag ;;first-attribute first value ;;second-attribue second value
second-tag Text inside the tag ;;first-attribute first value ;;second-attribute second value
 nested-tag Text inside nested tag ;;some-attribute some value
```
Output:

```xml
<first-tag first-attribute="first value" second-attribue="second value">
</first-tag>
<second-tag first-attribute="first value" second-attribute="second value">
 Text inside the tag
 <nested-tag some-attribute="some value">
  Text inside nested tag
 </nested-tag>
</second-tag>
```
