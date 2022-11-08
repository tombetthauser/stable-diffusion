# Stable Diffusion / Artist Collaborations

Collaborative experiments with visual artists and explanatory notes on machine learning concepts taken while building a custom stable diffusion implementation with the Python standard library.
* [artist collaboration 1](https://tombetthauser.github.io/stable-diffusion)
* [artist collaboration 2](https://tombetthauser.github.io/stable-diffusion/artist-2)

<!-- * [favorite output images](/assets/image-set-1/favorite-output-images.md) -->
<!-- * [all output images](/assets/image-set-1/all-output-images.md) -->
<!-- * [training images](/assets/image-set-1/training-images.md) -->

---

# What is Stable Diffusion?

Below are notes on stable diffusion, what it is, how it works and related machine learning concepts taken while working through a [Practical Deep Learning](https://course.fast.ai/) course. Their goal is to explain how Stable diffusion works in the simplest possible terms.

---

## Machine Learning Model

A computer program that is trained rather than being written manually.

<details>
  <summary>
  </summary><br>

  In it's simplest form, Machine Learning seems to just be a particular strategy for getting a computer to do a complex task. Say you want a computer to be able to do something like play chess or tell you if an image has a blue horse in it or not. A programmer tries to write some code that does this and realizes its crazy to try to manually code for every possible situation. So they pivot to a Machine Learning approach where they set up a training scenario that allows some code to write itself, making educated guesses on how to get the desired output with a wide variety of input and reinforcing itself in small parts when it's successful until it has a working version of itself. 

  This working version is often called a model and can consistently tell me what I wanted it to tell me, like if a random input image has a blue horse in it or not. They usually aren't perfect, maybe our blue horse identification model is accurate 92% of the time, but it can work consistently with literally any range input. if the programmer who set up this training scenario looked at the code inside the model they wouldn't necessarily have any idea why it was doing any individual thing it was doing, because they just coded the training not the model. This seems to cover what machine learning is in a very general sense, but is probably not a perfect explanation by any means. Head to [wikipedia](https://en.wikipedia.org/wiki/Machine_learning) for more obviously.

</details>


---


## Generative Models

<details>
  <summary>
    Models that produce complex outputs like writing and art.
  </summary><br>

  Generative Models [seem to be an extremely academic subject](https://en.wikipedia.org/wiki/Generative_model) that might lean more towards math than programming. But in practical computer programming terms they seem generally be a kind of reversal of identification models. For instance if a programmer trained a machine learning model to identify if there was a blue horse in an image it would spit out some kind of simple `yes, there's a blue horse in this image` or `no, there's no blue horse in this image`. If we were trying to make sure no one was allowed to post images of blue horses on a website or return a bunch of images of blue horses in search engine results this would be an extremely practical tool. But if we wanted to do something weirder that programmer could potentially reverse that model so that it took `yes, there's a blue horse in this image` as the input and then output a completely made up image that had a horse in it. This would be purely based on all the model's unintelligible internal code and would probably look a little weird since it wasn't directly based on anything real. This also doesn't have as many obvious practical applications, but it clearly seems to be a very powerful tool. 

</details>


---

## GPT-3

[GPT-3](https://en.wikipedia.org/wiki/GPT-3) is a text-generation model that can write essay-length text from very short prompts like 'Write a story about a secret forest full of unicorns.' The GPT stands for Generative Pre-trained Transformer.It's widely regarded to be capable of producing writing that is indistinguishable or nearly indistinguishable from an actual person's writing and has been identified as having dangerous societal implications. The New York Times has described GPT-3's capabilities as being able to write original prose with fluency equivalent to that of a human. 

It's the third generation model of the GPT-n series created by OpenAI in San Francisco and has been fully licensed by Microsoft since 2020. Individuals can still use it in limited amounts but code itself is not publicly accessible. Internally it uses a Transformer architecture, which seems to distinguish itself from other Machine Learning architectures by processing all the separate parts of it's input simultaneously rather than sequentially, like processing all three words in the input `colorless green ideas` rather than sequentially processing `colorless`, `green` then `ideas` in order. What that actually means seems difficult to get at from a non-academic perspective but that may have something to do with the fact that the source code is not publicly available.

---

## DALL-E

[DALL-E / DALL-E 2](https://en.wikipedia.org/wiki/DALL-E) is a text-to-image generative model also developed by OpenAI in San Francisco first released to limited public access in 2021. It uses a modified version of GPT-3 under the hood to produce images from written prompts. Similar to GPT-3 the code is not publicly available but is free for anyone to make a certain number of free uses of, then paying for additional uses. The name is a combination of `WALL-E` the robot Pixar character and `Salvador Dali` the 20th century painter. As a side-note `WALL-E` subsequently is an abbreviation of `Waste Allocation Load Lifter: Earth-Class` which may or may not mean anything. Like GPT-3 it's based on a Transformer architecture that seems to refer generally to processing individual parts of the input in parallel.

--

## Midjourney

[Midjourney](https://en.wikipedia.org/wiki/Midjourney) is a company whose primary product / focus is a text-to image generation model of the same name. They are based in San Francisco and entered an open beta phase in 2022 that allows people to make text-based requests to it's image generation model via Discord for free up to a limited point, after which they need to pay for additional requests.

As a potential point of interest, Midjourney's founder David Holz has stated that he sees visual artists as customers rather than competitors that might use text-to-image generation tools like Midjourney to rapidly prototype potential works for clients (or themselves) before committing to fully actualizing an artwork.

---

## Craiyon

An open-source text-to-image generation model / platform / tool developed by Hugging Face, a New York based company focused on developing open-source ai resources. It was previously named DALL-E mini but changed it's name after being requested to do so by the team that developed DALL-E / DALL-E 2.

---

## Stable Diffusion

Stable Diffusion is an open source text-to-image generation model developed at a University in Munich Germany. It's architecture and source code are public and will be explored in more detail in these notes.

<!-- ## DreamBooth -->
<!-- ## Imagen / Google Brain -->
<!-- ## Hugging Face -->

---

## DreamBooth

<details>
  <summary>
    A tool that allows you to put an object / person etc into an image.
  </summary><br>
</details>

---

## Diffusers

<details>
  <summary>
  </summary>The models that process between latents?<br>
</details> 

---

<!-- ## 
<details>
  <summary>
  </summary><br>
</details> 
--- -->