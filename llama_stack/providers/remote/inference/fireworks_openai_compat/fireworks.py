# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from llama_stack.providers.remote.inference.fireworks_openai_compat.config import FireworksCompatConfig
from llama_stack.providers.utils.inference.litellm_openai_mixin import LiteLLMOpenAIMixin

from ..fireworks.models import MODEL_ENTRIES


class FireworksCompatInferenceAdapter(LiteLLMOpenAIMixin):
    _config: FireworksCompatConfig

    def __init__(self, config: FireworksCompatConfig):
        LiteLLMOpenAIMixin.__init__(
            self,
            model_entries=MODEL_ENTRIES,
            api_key_from_config=config.api_key,
            provider_data_api_key_field="fireworks_api_key",
            openai_compat_api_base=config.openai_compat_api_base,
        )
        self.config = config

    async def initialize(self):
        await super().initialize()

    async def shutdown(self):
        await super().shutdown()
