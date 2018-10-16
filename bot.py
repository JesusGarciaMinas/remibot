import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import copy
warns = []
opciones_encuesta = 0
encuesta_data = {
	"enunciado" : "",
	"opciones" : {},
	"votos" : {},
	"votantes" : []
}

TOKEN = 'NTAwMDM5NTY1OTEwOTk5MDUw.DqKG0Q.GlyFoLpaYASvo1yuXVdk9O2ucdY'
Client = discord.Client()
client = commands.Bot(".")
command_prefix = "."

@client.event
async def on_ready():
	print("Bot is ready!")

@client.command(pass_context = True)
async def cookie(message):
	await client.say (":cookie:")

@client.command(pass_context = True)
async def encuesta(ctx):
	global command_prefix
	global encuesta_data
	encuesta_data = {
	"enunciado" : "",
	"opciones" : {},
	"votos" : {},
        "votantes" : []
	}
	datos = ctx.message.content.replace(command_prefix + "encuesta","")
	datos = datos.split("&")
	string = "{} a propuesto una encuesta\n{}".format(ctx.message.author.mention, datos[0])
	encuesta_data["enunciado"] = datos.pop(0)
	i = 0
	for option in datos:
		string += "\n{}.\t{}".format(chr(ord('A') + i),option)
		encuesta_data["opciones"][chr(ord('A') + i)] = option
		encuesta_data["votos"][chr(ord('A') + i)] = 0
		i = i + 1
	await client.say("{}".format(string))

@client.command(pass_context = True)
async def voto(ctx, opcion):
	global encuesta_data
	if not len(encuesta_data["opciones"]):
		await client.say("No hay encuesta cari :kissing_heart:")
		return
	if ctx.message.author in encuesta_data["votantes"]:
		await client.say("Ya has votado guapo :wink:")
		return
	if not opcion in encuesta_data["opciones"]:
		await client.say("Esa opcion no existe tontorron :flushed:")
		return
	encuesta_data["votantes"].append(ctx.message.author)
	encuesta_data["votos"][opcion] += 1
	await client.say("Voto recibido :clap::clap::clap:")

@client.command(pass_context = True)
async def resultados(ctx):
	i = 0
	global encuesta_data
	string = "{}".format(encuesta_data["enunciado"])
	for opcion in encuesta_data["opciones"]:
		string += "\n{}.\t{}\t{} Votos".format(chr(ord('A') + i), encuesta_data["opciones"].get(opcion), encuesta_data["votos"][chr(ord('A') + i)])
		i += 1
	await client.say("{}".format(string))


@client.command(pass_context = True)
async def mueve(ctx, userName: discord.User, channelName: discord.Channel):
	if ctx.message.author.server_permissions.manage_channels == 0:
		await client.say("Solo para admins crack, maquina, titan, monstruo")
		return
	await client.move_member(userName, channelName)
@client.command(pass_context = True)
async def chakick(ctx, *args : discord.User):
	if ctx.message.author.server_permissions.manage_channels == 0:
		await client.say("Solo para admins crack, maquina, titan, monstruo")
		return
	await client.create_channel(ctx.message.server, "Jail", type=discord.ChannelType.voice)
	await client.say('A casa guapo')
	for channel in ctx.message.server.channels:
		if channel.name == "Jail":
			for user in args:
				await client.move_member(user, channel)
			await client.delete_channel(channel)
			break

@client.command(pass_context = True)
async def strike(ctx, warned: discord.User):
	global warns
	warns.append(warned)
	if warns.count(warned) < 3:
		await client.say('Strike numero {} {}'.format(warns.count(warned), warned.mention))
	else:
		await client.create_channel(ctx.message.server, "Jail", type=discord.ChannelType.voice)
		for i in range(3):
			warns.remove(warned)
		await client.say('Strike numero 3 {} A casa guapo'.format(warned.mention))
		for channel in ctx.message.server.channels:
			if channel.name == "Jail":
				await client.move_member(warned, channel)
				await client.delete_channel(channel)
				break

@client.command(pass_context = True)
async def desalojo(ctx):
	if ctx.message.author.server_permissions.manage_channels == 0:
		await client.say("Solo para admins crack, maquina, titan, monstruo")
		return
	tmp = 0
	channel = []
	members = ctx.message.author.voice.voice_channel.voice_members.copy()
	for member in members:
		if member.id != ctx.message.author.id:
			tmp2 = False
			if len(channel) == 0:
				for channel4 in ctx.message.server.channels:
					channel.append(channel4)
			while tmp2 == False:
				for channel2 in channel:
					if channel2.type == discord.ChannelType.voice:
						if len(channel) > 0:
							if len(channel2.voice_members) == tmp:
								channel.remove(channel2)
								await client.move_member(member, channel2)
								tmp2 = True
								break
				if tmp2 == False:
					for channel5 in ctx.message.server.channels:
						channel.append(channel5)
					tmp += 1
@client.command(pass_context = True)
async def offmeta(ctx):
	f = open("data", "r")
	champs = f.read().split(", ")
	f.close()
	await client.say("{} te ha tocado {}".format(ctx.message.author.mention, random.choice(champs)))

@client.command(pass_context = True)
async def reunion(ctx):
	for member in ctx.message.server.members:
		if member.status.online:
			await client.move_member(member, ctx.message.channel)

client.run(TOKEN)
print("caca pedo culo pis");
