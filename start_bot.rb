#!/usr/bin/ruby

require 'telegram/bot'
token = '619070662:AAFA3ft3uzAyfPK5aiqJU5hvUNf-M93i6_A'
Telegram::Bot::Client.run(token) do |bot|
  bot.listen do |message|
    case message.text
    when '/start'
      bot.api.sendMessage(chat_id: message.chat.id, text: "Hello, #{message.from.first_name}")
    end
  end
end
