

# TODO: https://github.com/hwchase17/langchain/pull/3909
# TODO: You should implement the same but on the tools/base.py on the callback! (see the link above)

#
# class MyCustomHandlerOne(BaseCallbackHandler):
#     def on_llm_start(
#         self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
#     ) -> Any:
#
#         print(f"on_llm_start {prompts}")
#
#     def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
#         print(f"on_new_token {token}")
#
#     def on_llm_error(
#         self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
#     ) -> Any:
#         """Run when LLM errors."""
#
#     def on_chain_start(
#         self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
#     ) -> Any:
#         if 'agent_scratchpad' in inputs:
#             if inputs['agent_scratchpad']:
#                 print(inputs['agent_scratchpad'])
#                 # TODO: this is what make the trick
#                 # test = extract_html_text(inputs['agent_scratchpad'])
#                 # inputs['agent_scratchpad'] = test
#
#
#     def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
#         if 'agent_scratchpad' in outputs:
#             if outputs['agent_scratchpad']:
#                 print(outputs['agent_scratchpad'])
#         pass
#     def on_tool_start(
#         self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
#     ) -> Any:
#         print(f"on_tool_start {serialized['name']}")
#
#     def on_text(self, text: str, **kwargs: Any) -> Any:
#         return "Asd"
#         pass
#
#
#     def on_tool_end(
#         self,
#         output: str,
#         *,
#         run_id: UUID,
#         parent_run_id: Optional[UUID] = None,
#         **kwargs: Any,
#     ) -> Any:
#         # output = modify_string(output)
#         return output
#     def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
#         print(f"on_agent_action {action}")