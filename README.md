# Distance to the MKAD API
> *This is the result of the test set by Voctiv, to apply for the vacancy of Python developer.*

## Work description
I develop a Flask Blueprint to find the distance from the Moscow Ring Road to the specified address. The address is passed to the application in an HTTP request, if the specified address is located inside the MKAD, the distance does not need to be calculated.

## Technologies and explanation
- Python Flask Blueprint

I used the [Openrouteservice API](https://openrouteservice.org/) services to calculate the distance to the MKAD and for translate the given address to coordinates.

In addition, unit tests were performed with the unittest library.

## Functionality
There is just one endpoint, it's a post, you've to pass an address in a JSON, like in the example:
```json
{
	"address" : "Dolgoprudny, Óblast de Moscú, Rusia, 141703"
}
```
The address doesn't really have a specific format, but try to write it the better way you can, for expecting a better result.

### Result
You're going to receive another JSON like a response, but, as say in the test requirement, the result will be save in the *.log* file.
```json
{
  "distance": "62.69 Km"
}
```
And, if the given address it's inside the MKAD the result will be this (in the *.log* file it's save as **0**):
```json
{
  "distance": "It's inside the MKAD"
}
```

### ENDPOINTS
*API URL*: https://distance-to-mkad.herokuapp.com

> #### **POST**
`"/calculation/getdistance"`<br>
**REQUIREMENTS**
- JSON
```json
{
	"address" : "{THE ADDRESS}*"
}
```