{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7b17fa01-4eaa-43ba-938f-a6f252498c4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: openai in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (2.3.0)\n",
      "Requirement already satisfied: gradio in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (5.49.1)\n",
      "Requirement already satisfied: anyio<5,>=3.5.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (4.11.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (1.9.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (0.28.1)\n",
      "Requirement already satisfied: jiter<1,>=0.10.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (0.11.0)\n",
      "Requirement already satisfied: pydantic<3,>=1.9.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (2.11.10)\n",
      "Requirement already satisfied: sniffio in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (1.3.1)\n",
      "Requirement already satisfied: tqdm>4 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (4.67.1)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.11 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from openai) (4.15.0)\n",
      "Requirement already satisfied: idna>=2.8 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from anyio<5,>=3.5.0->openai) (3.11)\n",
      "Requirement already satisfied: certifi in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from httpx<1,>=0.23.0->openai) (2025.10.5)\n",
      "Requirement already satisfied: httpcore==1.* in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from httpx<1,>=0.23.0->openai) (1.0.9)\n",
      "Requirement already satisfied: h11>=0.16 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.16.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from pydantic<3,>=1.9.0->openai) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.33.2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from pydantic<3,>=1.9.0->openai) (2.33.2)\n",
      "Requirement already satisfied: typing-inspection>=0.4.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from pydantic<3,>=1.9.0->openai) (0.4.2)\n",
      "Requirement already satisfied: aiofiles<25.0,>=22.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (24.1.0)\n",
      "Requirement already satisfied: brotli>=1.1.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (1.1.0)\n",
      "Requirement already satisfied: fastapi<1.0,>=0.115.2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.119.0)\n",
      "Requirement already satisfied: ffmpy in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.6.3)\n",
      "Requirement already satisfied: gradio-client==1.13.3 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (1.13.3)\n",
      "Requirement already satisfied: groovy~=0.1 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.1.2)\n",
      "Requirement already satisfied: huggingface-hub<2.0,>=0.33.5 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.35.3)\n",
      "Requirement already satisfied: jinja2<4.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (3.1.6)\n",
      "Requirement already satisfied: markupsafe<4.0,>=2.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (3.0.3)\n",
      "Requirement already satisfied: numpy<3.0,>=1.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (2.3.4)\n",
      "Requirement already satisfied: orjson~=3.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (3.11.3)\n",
      "Requirement already satisfied: packaging in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (25.0)\n",
      "Requirement already satisfied: pandas<3.0,>=1.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (2.3.3)\n",
      "Requirement already satisfied: pillow<12.0,>=8.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (11.3.0)\n",
      "Requirement already satisfied: pydub in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.25.1)\n",
      "Requirement already satisfied: python-multipart>=0.0.18 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.0.20)\n",
      "Requirement already satisfied: pyyaml<7.0,>=5.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (6.0.3)\n",
      "Requirement already satisfied: ruff>=0.9.3 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.14.0)\n",
      "Requirement already satisfied: safehttpx<0.2.0,>=0.1.6 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.1.6)\n",
      "Requirement already satisfied: semantic-version~=2.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (2.10.0)\n",
      "Requirement already satisfied: starlette<1.0,>=0.40.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.48.0)\n",
      "Requirement already satisfied: tomlkit<0.14.0,>=0.12.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.13.3)\n",
      "Requirement already satisfied: typer<1.0,>=0.12 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.19.2)\n",
      "Requirement already satisfied: uvicorn>=0.14.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio) (0.37.0)\n",
      "Requirement already satisfied: fsspec in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio-client==1.13.3->gradio) (2025.9.0)\n",
      "Requirement already satisfied: websockets<16.0,>=13.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from gradio-client==1.13.3->gradio) (15.0.1)\n",
      "Requirement already satisfied: filelock in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from huggingface-hub<2.0,>=0.33.5->gradio) (3.20.0)\n",
      "Requirement already satisfied: requests in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from huggingface-hub<2.0,>=0.33.5->gradio) (2.32.5)\n",
      "Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from huggingface-hub<2.0,>=0.33.5->gradio) (1.1.10)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from pandas<3.0,>=1.0->gradio) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from pandas<3.0,>=1.0->gradio) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from pandas<3.0,>=1.0->gradio) (2025.2)\n",
      "Requirement already satisfied: click>=8.0.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from typer<1.0,>=0.12->gradio) (8.3.0)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from typer<1.0,>=0.12->gradio) (1.5.4)\n",
      "Requirement already satisfied: rich>=10.11.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from typer<1.0,>=0.12->gradio) (14.2.0)\n",
      "Requirement already satisfied: six>=1.5 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas<3.0,>=1.0->gradio) (1.17.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (4.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (2.19.2)\n",
      "Requirement already satisfied: mdurl~=0.1 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio) (0.1.2)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from requests->huggingface-hub<2.0,>=0.33.5->gradio) (3.4.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages (from requests->huggingface-hub<2.0,>=0.33.5->gradio) (2.5.0)\n",
      "* Running on local URL:  http://127.0.0.1:7860\n",
      "* Running on public URL: https://c86aa873bc9f4a4c3e.gradio.live\n",
      "\n",
      "This share link expires in 1 week. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"https://c86aa873bc9f4a4c3e.gradio.live\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Traceback (most recent call last):\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gradio/queueing.py\", line 759, in process_events\n",
      "    response = await route_utils.call_process_api(\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gradio/route_utils.py\", line 354, in call_process_api\n",
      "    output = await app.get_blocks().process_api(\n",
      "             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gradio/blocks.py\", line 2116, in process_api\n",
      "    result = await self.call_function(\n",
      "             ^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gradio/blocks.py\", line 1623, in call_function\n",
      "    prediction = await anyio.to_thread.run_sync(  # type: ignore\n",
      "                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/anyio/to_thread.py\", line 56, in run_sync\n",
      "    return await get_async_backend().run_sync_in_worker_thread(\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/anyio/_backends/_asyncio.py\", line 2485, in run_sync_in_worker_thread\n",
      "    return await future\n",
      "           ^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/anyio/_backends/_asyncio.py\", line 976, in run\n",
      "    result = context.run(func, *args)\n",
      "             ^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/gradio/utils.py\", line 915, in wrapper\n",
      "    response = f(*args, **kwargs)\n",
      "               ^^^^^^^^^^^^^^^^^^\n",
      "  File \"/var/folders/th/wqjsxyss0qb4j9ll94jbvl940000gn/T/ipykernel_2851/2077937606.py\", line 11, in CustomChatGPT\n",
      "    response = openai.ChatCompletion.create(\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/openai/lib/_old_api.py\", line 39, in __call__\n",
      "    raise APIRemovedInV1(symbol=self._symbol)\n",
      "openai.lib._old_api.APIRemovedInV1: \n",
      "\n",
      "You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.\n",
      "\n",
      "You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. \n",
      "\n",
      "Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`\n",
      "\n",
      "A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Created dataset file at: .gradio/flagged/dataset1.csv\n"
     ]
    }
   ],
   "source": [
    "!pip install openai gradio\n",
    "import openai\n",
    "import gradio as gr\n",
    "\n",
    "openai.api_key = \"your_api_key_here\"  # Replace with your key\n",
    "\n",
    "messages = [{\"role\": \"system\", \"content\": \"You are a helpful assistant.\"}]\n",
    "\n",
    "def CustomChatGPT(user_input):\n",
    "    messages.append({\"role\": \"user\", \"content\": user_input})\n",
    "    response = openai.ChatCompletion.create(\n",
    "        model=\"gpt-3.5-turbo\",\n",
    "        messages=messages\n",
    "    )\n",
    "    reply = response[\"choices\"][0][\"message\"][\"content\"]\n",
    "    messages.append({\"role\": \"assistant\", \"content\": reply})\n",
    "    return reply\n",
    "\n",
    "demo = gr.Interface(fn=CustomChatGPT, inputs=\"text\", outputs=\"text\", title=\"Intelligent Chatbot\")\n",
    "demo.launch(share=True)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df4a6a0f-87d3-4eb7-9943-872b427c38f9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
