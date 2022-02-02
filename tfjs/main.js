async function loadImage(url) {
  const img = new Image();
  img.src = url;
  return new Promise((resolve) => {
    img.onload = () => resolve(img);
  });
}

async function main() {
  const img = await loadImage("examples/hallway-0011.jpg");
  const model = await tf.loadLayersModel("model/model.json");
  console.log(model);
  const tensor = tf.browser.fromPixels(img);
  // Convert image pixels to float
  const tensor2 = tensor.toFloat().div(tf.scalar(255));
  //const resized = tf.image.resizeBilinear(tensor, [224, 224]);
  const input = tf.expandDims(tensor2);
  const result = await model.execute(input);
  const canvas = document.createElement("canvas");
  document.getElementById("container").appendChild(canvas);
  await tf.browser.toPixels(result.squeeze(), canvas);
}

main();
