# Stable Diffusion / Artist Collaborations

Collaborative experiments with visual artists and explanatory notes on machine learning concepts taken while building a custom stable diffusion implementation with the Python standard library.
* [artist collaboration 1](https://tombetthauser.github.io/stable-diffusion)
* [artist collaboration 2](https://tombetthauser.github.io/stable-diffusion/artist-2)

<!-- * [favorite output images](/assets/image-set-1/favorite-output-images.md) -->
<!-- * [all output images](/assets/image-set-1/all-output-images.md) -->
<!-- * [training images](/assets/image-set-1/training-images.md) -->

---

# What is Stable Diffusion?

Stable diffusion is computer program that can turn text into images, referred to as a machine learning or deep learning model. It was released in 2022 as an open source project, meaning anyone can read and make their own version of the source code. This is not the case for it's predecessors.

Below are notes on stable diffusion and related machine learning concepts taken while working through a [Practical Deep Learning](https://course.fast.ai/) course. They are in no particular order.

```⚠️ These notes are a work in progress!...```

---

## Machine Learning Model

A computer program that is trained rather than being written manually. Models are generally trained to accomplish a specific task using training data where the input and desired output is known. The internal logic of the trained program is treated like a black-box.

<details>
  <summary>more...</summary><br>
  In it's simplest form, Machine Learning seems to just be a particular strategy for getting a computer to do a complex task. Say you want a computer to be able to do something like play chess or tell you if an image has a blue horse in it or not. A programmer tries to write some code that does this and realizes its crazy to try to manually code for every possible situation. So they pivot to a Machine Learning approach where they set up a training scenario that allows some code to write itself, making educated guesses on how to get the desired output with a wide variety of input and reinforcing itself in small parts when it's successful until it has a working version of itself. 

  This working version is often called a model and can consistently tell me what I wanted it to tell me, like if a random input image has a blue horse in it or not. They usually aren't perfect, maybe our blue horse identification model is accurate 92% of the time, but it can work consistently with literally any range input. if the programmer who set up this training scenario looked at the code inside the model they wouldn't necessarily have any idea why it was doing any individual thing it was doing, because they just coded the training not the model. This seems to cover what machine learning is in a very general sense, but is probably not a perfect explanation by any means. Head to [wikipedia](https://en.wikipedia.org/wiki/Machine_learning) for more obviously.
</details>



## Generative Models

Machine learning models that are trained to produce complex outputs like writing and art. An image generation model might take an input like 'an astronaut riding a horse' and be able to produce thousands of convincing realistic images of this fictional scene.

<details>
  <summary>more...</summary><br>
  Generative Models [seem to be an extremely academic subject](https://en.wikipedia.org/wiki/Generative_model) that might lean more towards math than programming. But in practical computer programming terms they seem generally be a kind of reversal of identification models. For instance if a programmer trained a machine learning model to identify if there was a blue horse in an image it would spit out some kind of simple `yes, there's a blue horse in this image` or `no, there's no blue horse in this image`. If we were trying to make sure no one was allowed to post images of blue horses on a website or return a bunch of images of blue horses in search engine results this would be an extremely practical tool. But if we wanted to do something weirder that programmer could potentially reverse that model so that it took `yes, there's a blue horse in this image` as the input and then output a completely made up image that had a horse in it. This would be purely based on all the model's unintelligible internal code and would probably look a little weird since it wasn't directly based on anything real. This also doesn't have as many obvious practical applications, but it clearly seems to be a very powerful tool. 
</details>

## GPT-3

GPT-3 is a text-generation model that can write essay-length text from very short prompts. It stands for Generative Pre-trained Transformer and was released in 2020 by OpenAI in San Francisco and is now licensed exclusively to Microsoft. It is not open source but can be used freely in limited amounts.

<details>
  <summary>more...</summary><br>
  [GPT-3](https://en.wikipedia.org/wiki/GPT-3) is a text-generation model that can write essay-length text from very short prompts like 'Write a story about a secret forest full of unicorns.' The GPT stands for Generative Pre-trained Transformer. It's widely regarded to be capable of producing writing that is indistinguishable or nearly indistinguishable from an actual person's writing and has been identified as having dangerous societal implications. The New York Times has described GPT-3's capabilities as being able to write original prose with fluency equivalent to that of a human. 

  It's the third generation model of the GPT-n series created by OpenAI in San Francisco and has been fully licensed by Microsoft since 2020. Individuals can still use it in limited amounts but code itself is not publicly accessible. Internally it uses a Transformer architecture, which seems to distinguish itself from other Machine Learning architectures by processing all the separate parts of it's input simultaneously rather than sequentially, like processing all three words in the input `colorless green ideas` rather than sequentially processing `colorless`, `green` then `ideas` in order. What that actually means seems difficult to get at from a non-academic perspective but that may have something to do with the fact that the source code is not publicly available.
</details>


## DALL-E

[DALL-E / DALL-E 2](https://en.wikipedia.org/wiki/DALL-E) is a text-to-image generative model also developed by OpenAI in San Francisco first released to limited public access in 2021. It uses a modified version of GPT-3 under the hood to produce images from written prompts. Similar to GPT-3 the code is not publicly available but is free for anyone to make a certain number of free uses of, then paying for additional uses. The name is a combination of `WALL-E` the robot Pixar character and `Salvador Dali` the 20th century painter. As a side-note `WALL-E` subsequently is an abbreviation of `Waste Allocation Load Lifter: Earth-Class` which may or may not mean anything. Like GPT-3 it's based on a Transformer architecture that seems to refer generally to processing individual parts of the input in parallel.

--

## Midjourney

[Midjourney](https://en.wikipedia.org/wiki/Midjourney) is a company whose primary product / focus is a text-to image generation model of the same name. They are based in San Francisco and entered an open beta phase in 2022 that allows people to make text-based requests to it's image generation model via Discord for free up to a limited point, after which they need to pay for additional requests.

As a potential point of interest, Midjourney's founder David Holz has stated that he sees visual artists as customers rather than competitors that might use text-to-image generation tools like Midjourney to rapidly prototype potential works for clients (or themselves) before committing to fully actualizing an artwork.



## Craiyon

An open-source text-to-image generation model / platform / tool developed by Hugging Face, a New York based company focused on developing open-source ai resources. It was previously named DALL-E mini but changed it's name after being requested to do so by the team that developed DALL-E / DALL-E 2.



## Stable Diffusion

Stable Diffusion is an open source text-to-image generation model developed at a University in Munich Germany. It's architecture and source code are public and will be explored in more detail in these notes.

<!-- ## DreamBooth -->
<!-- ## Imagen / Google Brain -->
<!-- ## Hugging Face -->



## DreamBooth

<details>
  <summary>
    A tool that allows you to put an object / person etc into an image.
  </summary><br>
</details>



## Diffusers

<details>
  <summary>
    The library of stable diffusion tools freely provided by Hugging Face.
  </summary><br>

  Hugging face is not the only group / company that provides these kinds of tools / libraries but as of October 2022 they are the best and seem likely to continue to be. Working with other libraries in the future should be more-or-less similar though.

</details> 



## Pipeline

<details>
  <summary>
    A saved process that unifies a group of ordered machine learning functions.
  </summary><br>

    Sometimes referred to as a learner. Contains a bunch of automated processes like inference and models etc. You can save a pipeline to Hugging Face's library which they refer to as the hub. You can make your own and save it or use a pre-trained pipeline loaded from Hugging Face.

    Side note, Hugging Face saves things to the .cache folder in you home directory.
    
</details> 


## Inverence

<details>
  <summary>
    Another method for developing generative image models different from diffusion.
  </summary><br>
</details> 


## Guidance Scale

<details>
  <summary>
    A number that controls how much an input prompt is adhered.
  </summary><br>

  In stable diffusion a model will identify two sets of identified noise for each de-noising cycle. One that identifies noise unlike the prompt, and one that identifies noise that just generally makes the image not look like something real. It averages these two together based on the provided guidance scale.

  A guidance scale of 0 will result in strange images that look realistic in a general sense but look garbled and non-specific. A guidance scale of 10 can result in images that look overly generic or cartoon-simplified. A guidance scale of 7.5 seems to be the default standard.

</details> 


## Negative Prompt

<details>
  <summary>
    A prompt that will cause an object / color etc to not appear in output images.
  </summary><br>

  Similar to guidance scale a negative prompt will result in an additional set of identified noise representing the negative prompt object etc. This will be subtracted rather than averaged into the other identified noise which will result in the object not appearing in the final output.

</details> 


## Image to Image

<details>
  <summary>
    A kind of pipeline that accepts a sketch / image along with a prompt as it's starting point.
  </summary><br>
</details> 



## Fine Tuning

<details>
  <summary>
    A training data of images and text that piggy-backs on stable diffusion's functionality.
  </summary><br>

  Lambda Labs fine-tuned stable diffusion with a set of images of pokemon and auto-generated text like "green pokemon smiling". After training this the new fine-tuned model could accept a prompt like 'girl with a pearl earring' and output an image of that painting in the style of pokemon.

</details> 


## Textual Inversion

<details>
  <summary>
    A kind of fine tuning .
  </summary><br>

  Lambda Labs fine-tuned stable diffusion with a set of images of pokemon and auto-generated text like "green pokemon smiling". After training this the new fine-tuned model could accept a prompt like 'girl with a pearl earring' and output an image of that painting in the style of pokemon.

</details> 



## Finite Differencing

<details>
  <summary>
    An slow way to determine if changing an individual pixel makes an image more or less like something.
  </summary><br>

  Imagine a black box that takes an image as input and outputs a percentage chance that the input image contained a hand-written digit. If you gave it an image of pure noise / static, it might tell you there is a 0.02% chance that contains a handwritten number. If you made a few pixels darker or lighter, looking to connect darker areas into lines because handwritten numbers often contain lines, you could feed it back into our function and maybe raise the percentage chance to 0.08% and repeat the process until you had a good image of a number from a starting point of noise / static.

  If you wanted to automate this process with random guessing for each pixel, you could. And the more manual time-consuming version of the process of determining how to change each pixel to increase the percentage might be referred to as Finite Differencing.

  It seems this is essentially what we're doing with stable diffusion, but with more efficient python replacement for Finite Differencing.

</details> 



## Neural Net

<details>
  <summary>
    A neural net is what we use to train a function that we need rather than coding it manually.
  </summary><br>

  A neural net generally has inputs, outputs a loss function that updates weights using derivatives. [?]

  In stable diffusion, the training data starts with clear images of known objects / numbers etc with varying amounts of noise added on top of them so the desired output percentage is known. This seems like it could be used to train a function that either identifies the static in an image or the percentage of noise present.

</details> 



## Unet

<details>
  <summary>
    A type of neural net that forms the first key component of stable diffusion.
  </summary><br>

  Originally developed for medical imaging. The input for a unet is a somewhat noisy image and the output is just the noise.

</details> 



## Training Data

<details>
  <summary>
    Data sets used to train neural networks where the input and desired output is known. 
  </summary><br>
</details> 



## Convolution

<details>
  <summary>
    A process that compresses an image to a smaller version of itself. 
  </summary><br>

  Compressing an image down makes it more efficient to use as training data for a neural network. In stable diffusion we need a complementary inverse-convolution. In stable diffusion we trade height and width for depth.

  We can refer to these convolutions as convolutional layers or neural network layer.

</details> 



## Inverse-Convolution

<details>
  <summary>
    A process that uncompresses an image from a compressed version created by a convolution. 
  </summary><br>

  Compressing an image down makes it more efficient to use as training data for a neural network. In stable diffusion we need a complementary inverse-convolution. In stable diffusion we trade height and width for depth.

  We can refer to these convolutions as convolutional layers or neural network layer.

</details> 



## Auto-Encoder

<details>
  <summary>
    Refers to the combination of a set of convolutional and inverse-convolutional layers. 
  </summary><br>

  

</details> 



## Encoder / VAE

<details>
  <summary>
    An image compression algorithm made up of a series of convolution layers.
  </summary><br>
</details> 



## Decoder

<details>
  <summary>
    An image decompression algorithm made up of a series of inverse-convolution layers.
  </summary><br>
</details> 



## Latent

<details>
  <summary>
    The compressed version of an image after being run through an encoder.
  </summary><br>

  Latents seem similar to password hashes, except they can be reversed. So they are more like zipped versions of files. 

  The whole process of using latents in training neural networks is just for time-saving / efficiency and is not actually necessary in a situation with unlimited resources. You could just train the same neural network on the uncompressed images, it would just take exponentially longer to train.

</details> 




<!-- ## 
<details>
  <summary>
  </summary><br>
</details> 
 -->



# Code Exercises / Notebooks

## An Astronaut Riding a Horse
* download a pipeline from hugging face
* use it to create an astronaut riding a horse

