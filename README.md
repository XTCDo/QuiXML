# QuiXML
Easy xml formatting

## How to use
Run the `quixml.py` file inside any folder with `.txt` files. QuiXML will create formatted `.xml` files out of the `.txt` files.

QuiXML will overwrite any created `.xml` file when it detects a change in it's original `.txt` file.

**Make sure that you use a completely separate folder for QuiXML usage, you might accidentally overwrite other important `.xml` files!**
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
<first-tag/>
<second-tag>
 <nested-tag/>
</second-tag>
```

### Tags with content
Most tags, like `<h1>Title</h1>` in html for example usually have text inbetween the opening and closing tag

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
<first-tag first-attribute="first value" second-attribue="second value"/>
<second-tag first-attribute="first value" second-attribute="second value">
 Text inside the tag
 <nested-tag some-attribute="some value">
  Text inside nested tag
 </nested-tag>
</second-tag>
```

### Breaking lines
Sometimes you have a tag with a lot of attributes. If your editor does not wrap text, that can be annoying. You can insert `;n` at the end of a line to tell the program that the line below is part of the current line.

**Example**

Input:
```
first-tag ;;first-attribute first value ;n
;;second-attribute second value
second-tag
 nested-tag ;;first-attribute first value ;n
 ;;second-attribute second value
```
Output:

```xml
<first-tag first-attribute="first value" second-attribute="second value"/>
<second-tag>
 <nested-tag first-attribute="first value" second-attribute="second value"/>
</second-tag>
```

### Adding text
Sometimes you have text that doesn't go inside any tags like `Input: <input type="text" name="inputval"/>`

**Example**

Input:
```
first-tag
 ;t some text
 nested-tag text
 ;t more text
```
Output:

```xml
<first-tag>
 some text
 <nested-tag>
  text
 </nested-tag>
 more text
</first-tag>
```

### Automatic line breaks in XML
If an XML tag has more than three attributes or the line is longer than 50 characters and has at least 2 attributes. Those attributes will be placed on separate lines, automatically indented to match with the tag.

**Example**

Input:
```
first-tag ;;first-attribute first value ;;second-attribute second value ;n
 ;;third-attribute third value ;;fourth-attribute fourth value
second-tag ;;first-attribute first value ;;second-attribute second value ;;third-attribute third vale
third-tag ;;very-long-attribute-that-is-long very long value that is long ;;another-attribue another value
```
Output:

```xml
<first-tag first-attribute="first value"
           second-attribute="second value"
           third-attribute="third value"
           fourth-attribute="fourth value">
</first-tag>
<second-tag first-attribute="first value"
            second-attribute="second value"
            third-attribute="third vale">
</second-tag>
<third-tag very-long-attribute-that-is-long="very long value that is long" another-attribue="another value"/>
```
